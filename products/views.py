from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
    }

    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update(
            {'products': Product.objects.all()})
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # тоже самое, что и строчка выше
        # basket = Basket(user=request.user, product=product, quantity=1)
        # basket.save()
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    basket = Basket.objects.get(id=product_id)
    basket.delete()
    return HttpResponseRedirect(current_page)
