from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddPaperView.as_view(), name='add_paper'),
]
