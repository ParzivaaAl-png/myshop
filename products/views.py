from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    qs = Product.objects.filter(is_active=True)
    return render(request, 'products/list.html', {'products': qs})

def product_detail(request, slug):
    p = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/detail.html', {'product': p})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form, 'is_new': True})

def product_edit(request, slug):
    obj = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())
    else:
        form = ProductForm(instance=obj)
    return render(request, 'products/form.html', {'form': form, 'is_new': False, 'product': obj})
