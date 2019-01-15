

from index import views
from django.conf.urls import url
urlpatterns = [
    url('^$',views.index,name='index'),
    url('^about/$',views.about),
    url('^blog/$',views.blog),
    url('^contact/$',views.contact),
    url('^base/$',views.base)
]
