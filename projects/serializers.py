from rest_framework import serializers
from .models import Project, ProjectModule, ModuleTask


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModule
        fields = '__all__'


class ModuleTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleTask
        fields = '__all__'