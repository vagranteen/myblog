"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import path,re_path
from myblog import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newslistpic$', views.newslistpic),
    url(r'^about/$', views.about,name='about'),
    url(r'^listpic$', views.listpic),
    path('detail-<int:aid>.html', views.detail),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
