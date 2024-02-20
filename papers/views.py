from django.shortcuts import render
from .models import Paper


def paper_list(request):
    papers = Paper.objects.all().order_by('-publish_date')
    return render(request, 'papers/paper_list.html', {'papers': papers})
