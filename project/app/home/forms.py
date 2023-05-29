from django import forms
from . import models


class WriterForm(forms.ModelForm):
    class Meta:
        model = models.Writer
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
