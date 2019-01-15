from django.shortcuts import render
from index.models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    links = Link.objects.all().order_by('-id')
    return locals()


# 首页
def index(request):
    allarticle = Article.objects.all()
    # remen = Article.objects.all()
    tags = Tag.objects.all()
    links = Link.objects.all().order_by('-id')

    return render(request, 'index.html', locals())


def base(request):
    return render(request, 'base.html', locals())

    """ 
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    link = Link.objects.all()
    return render(request, 'index.html', locals())
    """


def tag(request, tag):
    """
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
     """
    return render(request, 'tags.html', locals())


def about(request):
    links = Link.objects.all().order_by('-id')
    return render(request, 'about.html', locals())


def blog(request):
    links = Link.objects.all().order_by('-id')
    allcategory = Category.objects.all()
    alltag = Tag.objects.all()
    return render(request, 'blog.html', locals())


def contact(request):
    links = Link.objects.all().order_by('-id')
    return render(request, 'contact.html', locals())
