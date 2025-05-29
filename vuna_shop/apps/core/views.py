from django.shortcuts import render
from apps.product.models import Product
# Create your views here.
def frontpage(request):
    newest_product = Product.objects.all()[0:8]
    print(f"newest_prod{newest_product}")
    return render(request,'core/frontpage.html', {'newest_product':newest_product})

def contact(request):
    return render(request,'core/contact.html')