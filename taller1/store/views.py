# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def create_product(request):
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success_created')
        else:
            form = ProductForm()

        return render(request, 'create_product.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

def success_created(request):
    return render(request, 'success_created.html')

def list_products(request):
    try:
        products = Product.objects.all()
        products_info = [
            {
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': product.price,
                'image_url': product.image.url if product.image else None,
            }
            for product in products
        ]

        return render(request, 'list_products.html', {'products': products_info})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

def view_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'view_product.html', {'product': product})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

def delete_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            product.delete()
            return redirect('list_products')
        return render(request, 'delete_product.html', {'product': product})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})
