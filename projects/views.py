from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    return render(
        request, "projects/list_projects.html", {"projects": projects}
    )
