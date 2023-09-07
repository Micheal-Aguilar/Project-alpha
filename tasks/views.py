from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "list_projects"
            )
    else:
        form = TaskForm()

    return render(request, "tasks/create_tasks.html", {"form": form})
