from django.urls import path
from .views import projectListAPIView, projectCreateAPIView, projectModuleListAPIView, projectModuleCreateAPIView, moduleTaskListAPIView, moduleTaskModuleCreateAPIView, projectListView, projectCreateView, projectModuleListView, projectModuleCreateView

urlpatterns = [
    path('api/v1/projects/', projectListAPIView),
    path('api/v1/projects/create', projectCreateAPIView),

    path('api/v1/modules/', projectModuleListAPIView),
    path('api/v1/modules/create', projectModuleCreateAPIView),

    path('api/v1/tasks/', moduleTaskListAPIView),
    path('api/v1/tasks/create', moduleTaskModuleCreateAPIView),

    #-------------------------  VIEWS -------------------------
    path('list/', projectListView, name='list-projects'),
    path('create/', projectCreateView, name='create-project'),

    path('module/list/', projectModuleListView, name='list-modules'),
    path('module/create/', projectModuleCreateView, name='create-module'),

]
