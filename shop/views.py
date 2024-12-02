from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def products_view(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})


def category_add_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Category.objects.create(title=title, description=description)
        return redirect('products_view')
    return render(request, 'shop/category_add.html')


def product_add_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')
        category = get_object_or_404(Category, id=category_id)
        Product.objects.create(
            title=title,
            description=description,
            category=category,
            price=price,
            image_url=image_url
        )
        return redirect('products_view')
    return render(request, 'shop/product_add.html', {'categories': categories})
