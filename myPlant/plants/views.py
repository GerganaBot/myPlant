from django.shortcuts import render, redirect

from myPlant.plants.forms import ProfileForm


def home_page(request):
    return render(request, template_name='plants/home-page.html')


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {'form': form}
    return render(request, template_name='plants/create-profile.html', context=context)


def edit_profile(request):
    return render(request, template_name='plants/edit-profile.html')


def delete_profile(request):
    return render(request, template_name='plants/delete-profile.html')


def details_profile(request):
    return render(request, template_name='plants/profile-details.html')


def catalogue(request):
    return render(request, template_name='plants/catalogue.html')


def create_plant(request):
    return render(request, template_name='plants/create-plant.html')


def details_plant(request):
    return render(request, template_name='plants/plant-details.html')


def edit_plant(request):
    return render(request, template_name='plants/edit-plant.html')


def delete_plant(request):
    return render(request, template_name='plants/delete-plant.html')



