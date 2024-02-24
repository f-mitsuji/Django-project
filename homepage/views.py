from django.views.generic import TemplateView, ListView
from django.db.models import Count, Prefetch
from papers.models import Paper, Comment


class HomePageView(TemplateView):
    template_name = 'homepage/home.html'


class HomePageView(ListView):
    model = Paper
    template_name = 'homepage/home.html'
    context_object_name = 'papers'

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related(
            Prefetch('comments', queryset=Comment.objects.all())
        ).annotate(
            comments_count=Count('comments'),
            unique_users_count=Count('comments__author', distinct=True)
        )
        return queryset
