from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})




def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})




def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list page after creating the task
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})







def task_update(request, pk):
    # Get the task object with the given primary key (pk) or return a 404 error if it doesn't exist
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = TaskForm(request.POST, instance=task)  # Bind the form with the task instance
        if form.is_valid():
            # If the form data is valid, save the form to update the task
            form.save()
            return redirect('task_list')  # Redirect to the task list page after updating the task
    else:
        # If the request method is GET, initialize the form with the task instance data
        form = TaskForm(instance=task)
    
    # Render the task update form template with the form and task objects
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})







def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to the task list page after deleting the task
    return render(request, 'tasks/task_delete.html', {'task': task})

