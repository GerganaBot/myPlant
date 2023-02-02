from django.urls import path, include
from myPlant.plants import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_plant, name='create-plant'),
    path('details/<int:id>/', views.details_plant, name='plant-details'),
    path('edit/<int:id>/', views.edit_plant, name='edit-plant'),
    path('delete/<int:id>/', views.delete_plant, name='delete-plant'),
    path('profile/', include([
        path('create/', views.create_profile, name='create-profile'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
        path('details/', views.details_profile, name='profile-details'),
    ]))

]
