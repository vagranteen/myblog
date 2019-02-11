from django.shortcuts import render
from myblog.models import Article


# Create your views here.
def index(request):
    allarticle = Article.objects.all()[:6]
    return render(request, 'myblog/index.html', locals())


def newslistpic(request):
    return render(request, 'myblog/newslistpic.html')


def about(request):
    return render(request, 'myblog/about.html')


def listpic(request):
    return render(request, "myblog/listpic.html")


def detail(request, aid):
    artice = Article.objects.get(id=aid)
    return render(request, "myblog/detail.html", locals())
