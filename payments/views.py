from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
import json
import logging

logger = logging.getLogger(__name__)

def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        phone_number = request.POST.get('phone_number')
        account_reference = 'AccountReference'
        transaction_desc = 'Payment Description'
        callback_url = settings.MPESA_CALLBACK_URL

        cl = MpesaClient()
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        # Handle response and save payment details
        if response['ResponseCode'] == '0':
            transaction_id = response['CheckoutRequestID']
            Payment.objects.create(
                user=request.user,
                amount=amount,
                transaction_id=transaction_id,
                status='Pending'
            )
            return redirect('payment_success')
        else:
            return redirect('payment_failed')

    return render(request, 'initiate_payment.html')

@csrf_exempt
def payment_confirmation(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the M-Pesa callback
            callback_data = json.loads(request.body)
            logger.info(f"Callback Data Received: {callback_data}")

            # Extract relevant details
            result_code = callback_data['Body']['stkCallback']['ResultCode']
            checkout_request_id = callback_data['Body']['stkCallback']['CheckoutRequestID']
            result_desc = callback_data['Body']['stkCallback']['ResultDesc']
            callback_metadata = callback_data['Body']['stkCallback'].get('CallbackMetadata', {}).get('Item', [])

            # Fetch the payment record based on the CheckoutRequestID
            try:
                payment = Payment.objects.get(transaction_id=checkout_request_id)
            except Payment.DoesNotExist:
                logger.error(f"Payment record not found for CheckoutRequestID: {checkout_request_id}")
                return JsonResponse({"error": "Payment record not found"}, status=404)

            # Update payment status based on the ResultCode
            if result_code == 0:
                # Payment was successful
                payment.status = "Completed"
                # Optionally, save additional details like receipt number
                for item in callback_metadata:
                    if item['Name'] == 'MpesaReceiptNumber':
                        payment.mpesa_receipt_number = item['Value']
                    if item['Name'] == 'PhoneNumber':
                        payment.phone_number = item['Value']
            else:
                # Payment failed
                payment.status = "Failed"

            payment.save()
            logger.info(f"Payment status updated: {payment.status} for transaction {checkout_request_id}")
            return JsonResponse({"message": "Payment status updated successfully"})

        except Exception as e:
            logger.error(f"Error processing payment confirmation: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
