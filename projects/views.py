from django.shortcuts import render, redirect
from .models import Project, ProjectModule, ModuleTask, Status
from .serializers import ProjectSerializer, ProjectModuleSerializer, ModuleTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
import requests


# List all the projects API 
@api_view(['GET'])
def projectListAPIView(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# Create a projects API 
@api_view(['POST'])
def projectCreateAPIView(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# List all the project modules API 
@api_view(['GET'])
def projectModuleListAPIView(request):
    projectModules = ProjectModule.objects.all()
    serializer = ProjectModuleSerializer(projectModules, many=True)
    return Response(serializer.data)


# Create a projects module API 
@api_view(['POST'])
def projectModuleCreateAPIView(request):
    serializer = ProjectModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# List all the project modules tasks API 
@api_view(['GET'])
def moduleTaskListAPIView(request):
    moduleTasks = ModuleTask.objects.all()
    serializer = ModuleTaskSerializer(moduleTasks, many=True)
    return Response(serializer.data)


# Create a projects module task API 
@api_view(['POST'])
def moduleTaskModuleCreateAPIView(request):
    serializer = ModuleTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# ----------------------------------------- VIEWS -----------------------------------------

def projectListView(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project/list.html', context)

def projectCreateView(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    if request.method == 'POST':
        api_url = "http://localhost:3000/project/api/v1/projects/create"

        
        project_name = request.POST.get('projectName')
        description = request.POST.get('description')
        created_by = request.POST.get('createdBy')
        assigned_manager = request.POST.get('assignedManager')
        status = request.POST.get('status')

        # Prepare data to be sent in the POST request
        data = {
            'project_name': project_name,
            'description': description,
            'created_by': created_by,
            'assigned_manager': assigned_manager,
            'status': status
        }

        response = requests.post(api_url, data=data)

        if response.status_code == 201:
            return redirect('projects/project/create.html', context)  
        
    return render(request, 'projects/project/create.html', context)


def projectModuleListView(request):
    modules = ProjectModule.objects.all()
    context = {
        'modules': modules
    }
    return render(request, 'projects/modules/list.html', context)



def projectModuleCreateView(request):
    users = User.objects.all()
    projects = Project.objects.all()
    context = {
        'users': users,
        'projects': projects
    }
    if request.method == 'POST':
        api_url = "http://localhost:3000/project/api/v1/modules/create"

        module_name = request.POST.get('moduleName')
        description = request.POST.get('description')
        team_lead = request.POST.get('teamLead')
        status = request.POST.get('status')
        project = request.POST.get('project')

        # Prepare data to be sent in the POST request
        data = {
            'module_name': module_name,
            'description': description,
            'status': status,
            'project': project,
            'team_lead': team_lead,
            
        }

        response = requests.post(api_url, data=data)

        if response.status_code == 201:
            return redirect('projects/modules/create.html', context)  
        
    return render(request, 'projects/modules/create.html', context)



# hw  do the same for the task.

