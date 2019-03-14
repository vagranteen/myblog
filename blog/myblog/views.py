from django.shortcuts import render
from myblog.models import Article, Category
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    indexArticles = Article.objects.all()
    indexArticless = Article.objects.all()[:5]
    page = request.GET.get('page')
    paginator = Paginator(indexArticles, 8)
    try:
        indexArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        indexArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        indexArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    ztArticles = Article.objects.all().order_by('-id')[:6]
    rankArticles = Article.objects.all().order_by('-views')[:8]
    refArticles = Article.objects.all()[:8]
    Articles_count = len(Article.objects.all())
    return render(request, 'index.html',locals())


def about(request):
    return render(request, 'about.html')


def diary(request):
    diaryArticles = Article.objects.filter(category_id__lt=5)

    page = request.GET.get('page')
    paginator = Paginator(diaryArticles, 7)
    try:
        diaryArticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        diaryArticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        diaryArticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    rankArticles = Article.objects.all().order_by('-views')[:8]
    refArticles = Article.objects.filter(category_id__lt=5).order_by('-views')[:8]

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


def blogroll(request):
    return render(request, 'blogroll.html')


def cpp(request):
    return render(request, 'cpp.html')


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
    refArticles = Article.objects.filter(category=1).order_by('-views')[:8]
    return render(request, 'java.html', locals())


def linux(request):
    return render(request, 'linux.html')


def python(request):
    return render(request, 'python.html')


def content(request, aid):
    article = Article.objects.get(id=aid)
    previous_blog = Article.objects.filter(create_time__gt=article.create_time, category=article.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=article.create_time, category=article.category.id).last()
    article.views = article.views + 1
    article.save()
    otherArticles = Article.objects.filter(category=article.category)[:11]
    rankArticles = Article.objects.all().order_by('-views')[:8]
    refArticles = Article.objects.filter(category=article.category).order_by('-views')[:8]

    return render(request, 'content.html', locals())

# def time(request):
#     return render(request, 'info.html')
#
# def search(request):
#     ss =