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
    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import ProjectForm
import json

from django.http import HttpResponseForbidden

@login_required
def user_projects(request, profile_id):
    # Ensure the logged-in user matches the requested profile_id
    
    

    profile = get_object_or_404(Profile, id=profile_id)
    if request.user.id != profile.user.id:
        return HttpResponseForbidden("You do not have permission to access this page.")
    projects = Project.objects.filter(profile=profile)

    # Handling new project creation
    if 'new_project' in request.GET:
        # Check if the current project is empty and delete if true
        current_project = projects.last()
        if current_project and not current_project.title and not current_project.description and not current_project.link:
            current_project.delete()

        new_project = Project(profile=profile)
        new_project.save()
        return redirect("user_projects", profile_id=profile_id)

    # Check if there are no projects and create an empty one
    if not projects.exists():
        empty_project = Project(profile=profile, title="Untitled Project")
        empty_project.save()
        # Redirect to refresh projects queryset
        return redirect("user_projects", profile_id=profile_id)

    project_id = request.GET.get('project_id')
    project = projects.first() if project_id is None else get_object_or_404(Project, pk=project_id, profile=profile)

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return redirect(f'/projects/user/{profile_id}/projects/?project_id={project.id}')
        elif 'delete' in request.POST:
            project.delete()
            return redirect(f'/projects/user/{profile_id}/projects/')
    else:
        form = ProjectForm(instance=project)

    projects_data = list(projects.values('id', 'title', 'description', 'link', 'image1', 'image2', 'image3'))
    current_project_index = projects.filter(id__lte=project.id).count()
    projects_count = projects.count()

    return render(request, 'projects/user_projects.html', {
        'profile': profile,
        'projects': projects,
        'form': form,
        'projects_json': json.dumps(projects_data),
        'current_project_id': project.id,
        'current_project_index': current_project_index,
        'projects_count': projects_count,
    })
