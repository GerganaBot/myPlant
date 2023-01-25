from django.shortcuts import render


def home_page(request):
    return render(request, template_name='plants/home-page.html')


def create_profile(request):
    return render(request, template_name='plants/create-profile.html')


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



