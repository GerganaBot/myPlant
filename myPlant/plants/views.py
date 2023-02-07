from django.shortcuts import render, redirect, get_object_or_404

from myPlant.plants.forms import ProfileForm, PlantForm, PlantDeleteForm
from myPlant.plants.models import Plant, Profile


def home_page(request):
    return render(request, template_name='plants/home-page-without-profile.html')


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()
        return redirect('catalogue')
    context = {'form': form}
    return render(request, template_name='plants/create-profile.html', context=context)


def edit_profile(request):
    return render(request, template_name='plants/edit-profile.html')


def delete_profile(request):
    return render(request, template_name='plants/delete-profile.html')


def details_profile(request):
    profile = get_object_or_404(Profile)
    plants = Plant.objects.all()
    plants_of_the_profile = plants.filter(to_profile=profile)

    context = {
        'profile': profile,
        'plants': plants,
        'plants_of_the_profile': plants_of_the_profile,
    }
    return render(request, template_name='plants/profile-details.html', context=context)


def catalogue(request):
    all_plants = Plant.objects.all()
    context = {
        'all_plants': all_plants
    }
    return render(request, template_name='plants/catalogue.html', context=context)


def create_plant(request):
    form = PlantForm(request.POST or None)
    if form.is_valid():
        plant = form.save(commit=False)
        profile = Profile.objects.get(pk=1)
        plant.to_profile = profile
        plant.save()
        return redirect('catalogue')
    context = {'form': form}
    return render(request, template_name='plants/create-plant.html', context=context)


def details_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    context = {
        'plant': plant,
    }
    return render(request, template_name='plants/plant-details.html', context=context)


def edit_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    if request.method == "GET":
        form = PlantForm(instance=plant, initial=plant.__dict__)
    else:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form}

    return render(request, template_name='plants/edit-plant.html', context=context)


def delete_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    if request.method == "POST":
        plant.delete()
        return redirect('catalogue')
    form = PlantDeleteForm(initial=plant.__dict__)
    for field in form.fields:
        form.fields[field].disabled = True
    context = {'form': form}
    return render(request, template_name='plants/delete-plant.html', context=context)






