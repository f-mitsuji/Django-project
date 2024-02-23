from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import urllib.request as request
import feedparser
from .models import Paper
from .forms import PaperForm
from dateutil import parser


def get_paper_info(arxiv_url):
    arxiv_id = arxiv_url.split('/abs/')[-1]
    base_url = 'http://export.arxiv.org/api/query?'
    query = f'id_list={arxiv_id}'
    url = base_url + query
    response = request.urlopen(url).read()
    feed = feedparser.parse(response)
    if feed.entries:
        entry = feed.entries[0]
        return {
            'title': entry.title,
            'author': ', '.join(author.name for author in entry.authors),
            'abstract': entry.summary,
            'published_at': entry.published,
            'arxiv_url': arxiv_url
        }
    else:
        return None


class AddPaperView(FormView):
    template_name = 'papers/add_paper.html'
    form_class = PaperForm
    success_url = reverse_lazy('add_paper')

    def form_valid(self, form):
        arxiv_url = form.cleaned_data.get('arxiv_url')

        paper_info = get_paper_info(arxiv_url)
        if not paper_info:
            print("失敗")
            return super().form_valid(form)

        try:
            published_at_date = parser.parse(paper_info['published_at']).date()
            Paper.objects.create(
                title=paper_info['title'],
                author=paper_info['author'],
                abstract=paper_info['abstract'],
                published_at=published_at_date,
                arxiv_url=arxiv_url,
                # user=self.request.user  # ログインしているユーザーを紐付ける場合
            )
        except Exception as e:
            print(f"論文の保存にエラー: {e}")

        return super().form_valid(form)
