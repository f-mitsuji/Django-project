from django import forms


class PaperForm(forms.Form):
    arxiv_url = forms.CharField(label='arXiv URL', max_length=100)
