# main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..studyCycles.models import StudyCycles
from ..textbooks.models import Textbooks
from ..subjects.models import Subjects
from ..webMaterials.models import WebMaterials
from .forms import SubjectForm
from ..textbooks.forms import TextbookFormSet
from ..webMaterials.forms import WebMaterialFormSet

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    return Response(data)

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
    return render(request, 'main/update_subject.html', {'form': form})

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
    return render(request, 'main/update_all_textbooks.html', {'formset': formset})

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
    return render(request, 'main/update_all_web_materials.html', {'formset': formset})
