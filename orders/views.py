from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from menuapp.models import MenuItem

@login_required
def place_order(request):
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item_id')
        quantity = int(request.POST.get('quantity', 1))
        menu_item = MenuItem.objects.get(id=menu_item_id)

        # Create an order if it doesn't exist
        order, created = Order.objects.get_or_create(
            customer=request.user, status='PENDING'
        )

        # Add item to the order
        OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        return redirect('track_orders')  # Redirect to the order tracking page

    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'place_order.html', {'menu_items': menu_items})


@login_required
def track_orders(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'track_orders.html', {'orders': orders})


@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user, status='COMPLETED').order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})
