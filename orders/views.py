from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from menuapp.models import MenuItem
from .forms import OrderFilterForm

@login_required
def place_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('menu_items')  # Get selected menu items
        quantities = request.POST.getlist('quantities')  # Get corresponding quantities

        if not selected_items:
            return render(request, 'place_order.html', {'menu_items': MenuItem.objects.filter(is_available=True), 'error': 'No items selected'})

        # Create a new order
        order = Order.objects.create(customer=request.user)

        for item_id, quantity in zip(selected_items, quantities):
            menu_item = MenuItem.objects.get(id=item_id)
            quantity = int(quantity)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        return redirect('track_orders')

    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'place_order.html', {'menu_items': menu_items})


@login_required
def track_orders(request):
    orders = Order.objects.filter(customer=request.user).prefetch_related('order_items__menu_item')
    return render(request, 'track_orders.html', {'orders': orders})


def order_list(request):
    form = OrderFilterForm(request.GET or None)
    orders = Order.objects.all()

    # Filter by status if provided
    if form.is_valid():
        status = form.cleaned_data.get('status')
        if status:
            orders = orders.filter(status=status)

    return render(request, 'order_list.html', {'form': form, 'orders': orders})