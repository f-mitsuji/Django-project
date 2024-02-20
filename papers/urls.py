from django.urls import path
from . import views

urlpatterns = [
    path('', views.paper_list, name='paper_list'),
]
