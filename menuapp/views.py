from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, MenuItem
from .forms import CategoryForm, MenuItemForm
from django.http import HttpResponse


# Display menu with categories and items
def menu1(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu1.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page after saving
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page after saving
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

def edit_item(request, item_id):
    # Logic to edit the item
    item = get_object_or_404(MenuItem, id=item_id)
    # Render an edit form or process submitted changes
    return HttpResponse("Edit item functionality here.")

def delete_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(MenuItem, id=item_id)
        item.delete()
        return redirect('menu')  # Redirect to the menu page
    return HttpResponse("Invalid request method.", status=405)

def adminmenuc(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'adminmenuc.html', {'categories': categories})
