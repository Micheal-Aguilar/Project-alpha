from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list_projects.html", context)


@login_required(login_url="/accounts/login/")
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project": project}
    return render(request, "projects/detail_projects.html", context)
