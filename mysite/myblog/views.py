from django.shortcuts import render
from myblog.models import Article


# Create your views here.
def index(request):
    allarticle = Article.objects.all()[:6]
    rankartic = Article.objects.all().order_by('-views')
    return render(request, 'myblog/index.html', locals())


def about(request):
    return render(request, 'myblog/about.html')


def detail(request, aid):
    artice = Article.objects.get(id=aid)
    allarticle = Article.objects.all()[:6]
    rankartic = Article.objects.all().order_by('-views')
    return render(request, "myblog/detail.html", locals())


def listartic(request):
    rankartic = Article.objects.all().order_by('-views')
    allarticle = Article.objects.all()[:6]
    return render(request, 'myblog/listartic.html', locals())
