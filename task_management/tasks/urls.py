from django.urls import path
from .views import TaskView, TaskCreateView, TaskDetailView, TaskUpdateStatusView, CommentCreateView

urlpatterns = [
    path('', TaskView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update-status/', TaskUpdateStatusView.as_view(), name='update_task_status'),
    path('task/<int:task_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
]
