from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать',
        'username': 'Иван Иванов',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090.00
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': 23725.00
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390.00
            },
        ],
        'promotion': True,
        'products_of_promotion': [
            {
                'name': 'Белый спортивный костюм Nike',
                'price': 15390.00
            },
        ]
    }
    return render(request, 'products/test-context.html', context)
