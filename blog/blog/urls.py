from django.contrib import admin
from django.urls import path

urlpatterns = [
 path('admin/', admin.site.urls),
 path(r'^article/(?P<article_id>\d+)$', views.get_article,  name='get_article'),
 path('', views.home, name='home'), 
]