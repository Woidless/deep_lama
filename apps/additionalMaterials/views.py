# additionalMaterials/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AdditionalMaterials
from .forms import AdditionalMaterialsForm

@login_required
def additional_materials_create(request):
    if request.method == 'POST':
        form = AdditionalMaterialsForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.added_by = request.user
            material.save()
            return redirect('additional_materials_list')
    else:
        form = AdditionalMaterialsForm()
    return render(request, 'additionalMaterials/additional_materials_form.html', {'form': form})

def additional_materials_list(request):
    materials = AdditionalMaterials.objects.all()
    return render(request, 'additionalMaterials/additional_materials_list.html', {'materials': materials})

def additional_materials_detail(request, pk):
    material = get_object_or_404(AdditionalMaterials, pk=pk)
    return render(request, 'additionalMaterials/additional_materials_detail.html', {'material': material})

@login_required
def additional_materials_update(request, pk):
    material = get_object_or_404(AdditionalMaterials, pk=pk)
    if request.method == 'POST':
        form = AdditionalMaterialsForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('additional_materials_detail', pk=material.pk)
    else:
        form = AdditionalMaterialsForm(instance=material)
    return render(request, 'additionalMaterials/additional_materials_form.html', {'form': form})

@login_required
def additional_materials_delete(request, pk):
    material = get_object_or_404(AdditionalMaterials, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('additional_materials_list')
    return render(request, 'additionalMaterials/additional_materials_confirm_delete.html', {'material': material})