# subjects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subjects

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, 'Subject and all related materials have been deleted.')
        return redirect('view_subjects')
    return render(request, 'subjects/subject_confirm_delete.html', {'subject': subject})
