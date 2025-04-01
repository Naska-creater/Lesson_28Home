from django import forms
from .models import Task, User, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'completed_at']

    assignee = forms.ModelChoiceField(queryset=User.objects.all(), required=True, label="Исполнитель")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']