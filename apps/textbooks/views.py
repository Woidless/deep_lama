from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TextbookForm, SelectSubjectForm, SelectTextbookForm
from .models import Textbooks

@login_required
def create_textbook(request):
    if request.method == 'POST':
        form = TextbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')
    else:
        form = TextbookForm()
    return render(request, 'textbooks/create_textbook.html', {'form': form})


@login_required
def delete_textbook(request):
    if request.method == 'POST':
        subject_form = SelectSubjectForm(request.POST)
        if 'subject' in request.POST:
            subject_id = request.POST.get('subject')
            textbooks = Textbooks.objects.filter(subject_id=subject_id)
            textbook_form = SelectTextbookForm(request.POST, textbooks=textbooks)
            if textbook_form.is_valid():
                textbook_id = textbook_form.cleaned_data['textbook']
                textbook = get_object_or_404(Textbooks, id=textbook_id)
                textbook.delete()
                return redirect('view_subjects')
        else:
            textbook_form = None
    else:
        subject_form = SelectSubjectForm()
        textbook_form = None
    return render(request, 'textbooks/delete_textbook.html', {
        'subject_form': subject_form,
        'textbook_form': textbook_form
    })