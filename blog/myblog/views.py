from django.shortcuts import render
from myblog.models import Article, Category,Link
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.hashers import make_password




# Create your views here.

def index(request):
    indexArticles = Article.objects.all()
    newArticles = Article.objects.all().order_by("-create_time")[:5]
    page = request.GET.get('page')
    paginator = Paginator(indexArticles, 8)
    try:
        indexArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        indexArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        indexArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    ztArticles = Article.objects.all().order_by('-id')[:6]

    #右侧内容
    Articles_count = len(Article.objects.all()) #文章总数
    rankArticles = Article.objects.all().order_by('-views')[:8] #点击排行
    recommendArticle = Article.objects.filter(tui=2).order_by('-create_time')[:8]#站长推荐
    guessYouLike = Article.objects.filter(tui=3).order_by('-create_time')[:8]#彩泥喜欢
    blogroll = Link.objects.all() #友情链接

    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')


def diary(request):
    javaArticles = Article.objects.filter(category=1)[:6]
    cpprticles = Article.objects.filter(category=2)[:6]
    pythonArticles = Article.objects.filter(category=3)[:6]
    linuxArticles = Article.objects.filter(category=4)[:6]
    databasesArticles = Article.objects.filter(category=5)[:6]
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.all().order_by('-create_time')[:8]
    blogroll = Link.objects.all()

    return render(request, 'diary.html', locals())


def track(request):
    trackArticles = Article.objects.filter(category=7)

    trackArticles_count = len(Article.objects.filter(category=8).annotate(Sum("id")))

    page = request.GET.get('page')
    paginator = Paginator(trackArticles, 7)
    try:
        trackArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        trackArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        trackArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    rankArticles = Article.objects.all().order_by('-views')[:8]
    refArticles = Article.objects.filter(category=7).order_by('-views')[:8]

    return render(request, 'track.html', locals())


def life(request):
    return render(request, 'life.html')



def cpp(request):
    cppArticles = Article.objects.filter(category=2)
    page = request.GET.get('page')
    paginator = Paginator(cppArticles, 7)
    try:
        cppArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        cppArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        cppArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.filter(category=2).order_by('-create_time')[:8]


    return render(request, 'cpp.html', locals())


def java(request):
    javaArticles = Article.objects.filter(category=1)
    page = request.GET.get('page')
    paginator = Paginator(javaArticles, 7)
    try:
        javaArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        javaArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        javaArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.filter(category=1).order_by('-create_time')[:8]

    return render(request, 'java.html', locals())


def linux(request):
    linuxArticles = Article.objects.filter(category=4)
    page = request.GET.get('page')
    paginator = Paginator(linuxArticles, 7)
    try:
        linuxArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        linuxArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        linuxArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.filter(category=4).order_by('-create_time')[:8]

    return render(request, 'linux.html', locals())


def python(request):
    pythonArticles = Article.objects.filter(category=3)
    page = request.GET.get('page')
    paginator = Paginator(pythonArticles, 7)
    try:
        pythonArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        pythonArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        pythonArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.filter(category=3).order_by('-create_time')[:8]

    return render(request, 'python.html', locals())

#内容

def content(request, aid):
    article = Article.objects.get(id=aid)
    previous_blog = Article.objects.filter(create_time__gt=article.create_time, category=article.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=article.create_time, category=article.category.id).last()
    article.views = article.views + 1
    article.save()

    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.all().order_by('-create_time')[:8]


    return render(request, 'content.html', locals())


#查找
def search(request):
    kw = request.GET.get('keyboard')
    ssArticles = Article.objects.filter(title__contains=kw)
    page = request.GET.get('page')
    paginator = Paginator(ssArticles, 8)
    try:
        ssArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        ssArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        ssArticles = paginator.page(paginator.num_pages)
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.all().order_by('-create_time')[:8]
    blogroll = Link.objects.all()

    return render(request, 'search.html', locals())

def databases(request):
    databasesrticles = Article.objects.filter(category=5)
    page = request.GET.get('page')
    paginator = Paginator(databasesrticles, 7)
    try:
        databasesrticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        databasesrticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        databasesrticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    recommendArticle = Article.objects.filter(category=5).order_by('-create_time')[:8]

    return render(request, 'databases.html', locals())