# PMS

- models
  - Project - 1-M w/ Module
  - Module - 1-M w/ Tasks and M-1 w/Projects on project_id
  - Tasks M-1 w/ Module on module_id

### API Endpoint

- /api/project/project/create - POST request to create project
- /api/project/projects - GET request to list all projects

- /api/projects/modules - GET request to list all modules
- /api/projects/module/create - POST request to create a module

- /api/projects/tasks - GET request to list all tasks
- /api/projects/task/create - POST request to create a task

### Views

- project/project/create/
- project/project/list/

- project/module/create/
- project/module/list/
