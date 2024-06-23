# curriculum/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ..studyCycles.models import StudyCycles
from ..textbooks.models import Textbooks
from ..subjects.models import Subjects
from ..webMaterials.models import WebMaterials
from .forms import SubjectForm, TextbookForm

from ..textbooks.forms import TextbookFormSet
from ..webMaterials.forms import WebMaterialFormSet

from django.forms import modelformset_factory

@login_required
def view_subjects(request):
    study_cycles = StudyCycles.objects.all()
    data = []
    for study_cycle in study_cycles:
        subjects_data = []
        subjects = Subjects.objects.filter(study_cycle=study_cycle)
        for subject in subjects:
            textbooks = Textbooks.objects.filter(subject=subject)
            web_materials = WebMaterials.objects.filter(subject=subject)
            textbooks_info = [{"name": textbook.name, "quantity": textbook.quantity} for textbook in textbooks]
            subjects_data.append({
                'subject_id': subject.id,
                'subject_name': subject.name,
                'education_form': subject.education_form.name,
                'number_of_students': subject.number_of_students,
                'textbooks': textbooks_info,
                'web_materials': [web_material.web_link for web_material in web_materials],
            })
        data.append({
            'study_cycle': study_cycle.name,
            'subjects': subjects_data,
        })
    return render(request, 'curriculum/subjects.html', {'data': data})

@login_required
def update_subject(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'curriculum/update_subject.html', {'form': form})

@login_required
def update_all_textbooks(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    if request.method == 'POST':
        formset = TextbookFormSet(request.POST, queryset=Textbooks.objects.filter(subject=subject))
        if formset.is_valid():
            formset.save()
            return redirect('view_subjects')
    else:
        formset = TextbookFormSet(queryset=Textbooks.objects.filter(subject=subject))
    return render(request, 'curriculum/update_all_textbooks.html', {'formset': formset})

@login_required
def update_all_web_materials(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    if request.method == 'POST':
        formset = WebMaterialFormSet(request.POST, queryset=WebMaterials.objects.filter(subject=subject))
        if formset.is_valid():
            formset.save()
            return redirect('view_subjects')
    else:
        formset = WebMaterialFormSet(queryset=WebMaterials.objects.filter(subject=subject))
    return render(request, 'curriculum/update_all_web_materials.html', {'formset': formset})


@login_required
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')
    else:
        form = SubjectForm()
    return render(request, 'curriculum/create_subject.html', {'form': form})


@login_required
def delete_textbook(request, textbook_id):
    textbook = get_object_or_404(Textbooks, id=textbook_id)
    subject_id = textbook.subject.id  # Get subject ID before deletion
    if request.method == 'POST':
        textbook.delete()
        # Redirect to the subject detail page or any other desired page
        return redirect('view_subjects')
    else:
        # Optionally, handle GET request for confirmation before deletion
        return render(request, 'curriculum/confirm_delete_textbook.html', {'textbook': textbook})


@login_required
def delete_textbooks(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    TextbookFormSet = modelformset_factory(Textbooks, form=TextbookForm, extra=0)

    if request.method == 'POST':
        formset = TextbookFormSet(request.POST, queryset=Textbooks.objects.filter(subject=subject))
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('delete_textbook'):
                    textbook_id = form.instance.id
                    Textbooks.objects.filter(id=textbook_id).delete()
            return redirect('view_subjects')
    else:
        formset = TextbookFormSet(queryset=Textbooks.objects.filter(subject=subject))

    return render(request, 'curriculum/delete_textbooks.html', {'formset': formset})