from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_key = request.GET.get('sort')
    sort_order = request.GET.get('order', 'asc')
    if sort_key == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_key == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_key == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort_key == 'release_date':
        if sort_order == 'asc':
            phones = Phone.objects.order_by('release_date')
            sort_order = 'desc'
        else:
            phones = Phone.objects.order_by('-release_date')
            sort_order = 'asc'
    else:
        phones = Phone.objects.all()
    context = {'phones': phones, 'sort_order': sort_order}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
