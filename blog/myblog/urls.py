from django.conf.urls import url
from myblog import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('diary/', views.diary, name='diary'),
    path('track/', views.track, name='track'),
    path('life/', views.life, name='life'),

    path('search/', views.search, name='search'),
    path('diary/cpp/', views.cpp),
    path('diary/java/', views.java),
    path('diary/linux/', views.linux),
    path('diary/python/', views.python),
    path('diary/databases/', views.databases),

    path('diary/databases/content-<int:aid>.html', views.content),
    path('diary/数据库/content-<int:aid>.html', views.content),
    path('diary/java/content-<int:aid>.html', views.content),
    path('diary/track/content-<int:aid>.html', views.content),
    path('diary/点滴生活/content-<int:aid>.html', views.content),
    path('diary/我的足记/content-<int:aid>.html', views.content),
    path('diary/life/content-<int:aid>.html', views.content),

]
