from django.urls import path

from . import views

app_name = "papers"

urlpatterns = [
    path("add/", views.AddPaperView.as_view(), name="add_paper"),
    path("", views.PaperListView.as_view(), name="paper_list"),
    path("<int:pk>/", views.PaperDetailView.as_view(), name="paper_detail"),
]
