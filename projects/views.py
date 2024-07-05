from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from profiles.models import Profile
import json

def view_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    profile = project.profile

    return render(request, 'projects/view_project.html', {
        'project': project,
        'profile': profile,
    })
@login_required
def user_projects(request, user_id):
    if request.user.id != user_id:
        return redirect('home')  # or show a 403 error

    profile = get_object_or_404(Profile, user_id=user_id)
    projects = Project.objects.filter(profile=profile)
    
    project_id = request.GET.get('project_id')
    project = projects.first() if project_id is None else get_object_or_404(Project, pk=project_id, profile=profile)

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return redirect('user_projects', user_id=user_id)
        elif 'delete' in request.POST:
            project.delete()
            return redirect('user_projects', user_id=user_id)
        elif 'new' in request.POST:
            new_project = Project(profile=profile)
            new_project.save()
            return redirect('user_projects', user_id=user_id)
    else:
        form = ProjectForm(instance=project)

    projects_data = list(projects.values('id', 'title', 'description', 'link', 'image1', 'image2', 'image3'))

    return render(request, 'projects/user_projects.html', {
        'form': form,
        'projects_json': json.dumps(projects_data),
        'current_project_id': project.id if project else None,
    })