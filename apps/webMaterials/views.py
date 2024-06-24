from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WebMaterialForm, SelectSubjectForm, SelectWebMaterialForm
from .models import WebMaterials
from apps.subjects.models import Subjects

@login_required
def create_web_material(request):
    if request.method == 'POST':
        form = WebMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')
    else:
        form = WebMaterialForm()
    return render(request, 'webMaterials/create_web_material.html', {'form': form})

@login_required
def delete_web_material(request):
    if request.method == 'POST':
        subject_form = SelectSubjectForm(request.POST)
        if 'subject' in request.POST:
            subject_id = request.POST.get('subject')
            web_materials = WebMaterials.objects.filter(subject_id=subject_id)
            web_material_form = SelectWebMaterialForm(request.POST, web_materials=web_materials)
            if web_material_form.is_valid():
                web_material_id = web_material_form.cleaned_data['web_material']
                web_material = get_object_or_404(WebMaterials, id=web_material_id)
                web_material.delete()
                return redirect('view_subjects')
        else:
            web_material_form = None
    else:
        subject_form = SelectSubjectForm()
        web_material_form = None
    return render(request, 'webMaterials/delete_web_material.html', {
        'subject_form': subject_form,
        'web_material_form': web_material_form
    })