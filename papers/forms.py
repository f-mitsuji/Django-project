from django import forms

from .models import Comment


class PaperForm(forms.Form):
    arxiv_url = forms.CharField(label="arXiv URL", max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
