from django.shortcuts import render, get_object_or_404, redirect
import random
from django.db.models import Q
from .models import Category, Product
from .forms import AddToCartForm
from django.contrib import messages
from apps.cart.cart import Cart
# Create your views here.
def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))

    return render(request, 'products/search.html', {'products':products, 'query':query})


def product(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, category__slug=category_slug, slug = product_slug)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, "The product was added to the cart")
            return redirect('product', category_slug= category_slug, product_slug = product_slug)
    else:
        form = AddToCartForm()
    
    similar_products = list(product.category.products.exclude(id = product.id))

    if len(similar_products) >=4:
        similar_products = random.sample(similar_products,4)

    return render(request,'products/product.html', {'form': form, 'product':product, 'similar_products':similar_products})


def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    return render(request, 'products/category.html', {'category':category})

