from django import forms
from myPlant.plants.models import Profile, Plant


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['to_profile']


class PlantDeleteForm(PlantForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
