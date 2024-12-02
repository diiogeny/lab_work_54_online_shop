from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def products_view(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def product_details_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/details.html', {'product': product})

def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = CategoryForm()
    return render(request, 'shop/add_category.html', {'form': form})
