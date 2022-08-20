from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page-about', views.about, name='about'),
    path('detail',views.detail),
    path('create', views.create, name='create'),
    path('newcreate', views.newcreate, name='newcreate'),
]