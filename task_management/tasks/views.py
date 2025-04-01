from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .forms import TaskForm, CommentForm
from .models import Task


class TaskView(View):

    def get (self, request):
        tasks = Task.objects.all().order_by('-created_at')
        return render(request, 'tasks/task_list.html', {'tasks': tasks})

class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'tasks/create_task.html', {'form': form})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskUpdateStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        new_status = request.POST.get('status')

        if new_status in ['In Progress', 'Completed']:
            task.status = new_status
            task.save()
            return redirect('task_detail', pk=task.pk)

        return redirect('task_detail', pk=task.pk)

class CommentCreateView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
        return redirect('task_detail', task_id=task.id)