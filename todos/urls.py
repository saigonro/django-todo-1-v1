from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details),
    path('add', views.add, name='add')
    # url(r'^details/(?P<id>\w{0,50})/$', views.details),
]
