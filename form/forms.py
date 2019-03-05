from django.forms import ModelForm ,Textarea
from .models import Profile

# Create the form class.
class ProfileForm(ModelForm):

     class Meta:
         model = Profile
         fields = ['name', 'adm_no', 'email', 'phno','image1','image2','image3']

     # widgets = {
     #        'name': Textarea(attrs={'class': 'form-control', 'placeholder': 'Name'}),
     #        'adm_no': Textarea(attrs={'class': 'form-control', 'placeholder': 'Admission_No'}),
     #        'email': Textarea(attrs={'class': 'form-control', 'placeholder': 'Email'}),
     #        'phno': Textarea(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
     #        'image': Textarea(attrs={'class': 'form-control', 'placeholder': 'Image'})           
     #    }    