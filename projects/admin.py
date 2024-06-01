from django.contrib import admin
from projects.models import Project, ProjectModule, ModuleTask

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectModule)
admin.site.register(ModuleTask)