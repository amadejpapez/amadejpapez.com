from django.shortcuts import render

# Create your views here.
def main_view(request, *args, **kwargs):
        return render(request, "main.html", {})

def projects_view(request, *args, **kwargs):
        return render(request, "projects.html", {})