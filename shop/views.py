from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm, ProductSearchForm

def products_view(request):
    form = ProductSearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['search']
        products = Product.objects.filter(title__icontains=search_query, stock__gte=1).order_by('category__name', 'title')
    else:
        products = Product.objects.filter(stock__gte=1).order_by('category__name', 'title')
    return render(request, 'shop/products.html', {'products': products, 'form': form})

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

def edit_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/edit_product.html', {'form': form})

def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    return render(request, 'shop/delete_product.html', {'product': product})

