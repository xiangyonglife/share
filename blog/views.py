from django.shortcuts import render


# Create your views here.
def layout(request):
    return render(request, 'layout.html')


def index(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'article_detail.html')
