from django.conf.urls import url

from home import views
#from home.views import index

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
