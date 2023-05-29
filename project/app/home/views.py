from django.shortcuts import redirect, render
from . import forms


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def create_writer(request):
    if request.method == "POST":
        form = forms.WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.WriterForm()
    return render(request, "home/create_writer.html", {"form": form})


def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.PostForm()
    return render(request, "home/create_post.html", {"form": form})
