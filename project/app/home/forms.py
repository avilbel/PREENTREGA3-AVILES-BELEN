from django import forms
from . import models


class Writerform(forms.ModelForm):
    class Meta:
        model = models.Writer
        fields = "__all__"


class Postform(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
