from django.db import models
from django.contrib.auth.models import User


class Status(models.IntegerChoices):
    NOT_STARTED = 0, 'Not Started'
    IN_PROGRESS = 1, 'In Progress'
    COMPLETED = 2, 'Completed'
    CANCELLED = 3, 'Cancelled'

# projects 
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_STARTED)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.CASCADE)
    assigned_manager = models.ForeignKey(User, related_name='managed_projects', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.project_name

# modules
class ProjectModule(models.Model):
    project = models.ForeignKey(Project, related_name='modules', on_delete=models.CASCADE)
    module_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_STARTED)
    team_lead = models.ForeignKey(User, related_name='module_lead', on_delete=models.SET_NULL, null=True, blank=True)
   

    def __str__(self):
        return self.module_name


# tasks
class ModuleTask(models.Model):
    project_module = models.ForeignKey(ProjectModule, related_name='tasks', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_by = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_STARTED)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.task_name
    

# homework
# - 1. find what does related_name do in django models