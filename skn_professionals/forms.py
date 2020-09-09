from django import forms
from skn_professionals.models import ProfessionalProfile, RecommendProfessional


class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        exclude = ['user', 'nationality', 'created_on', 'admin_approved']



class RecommendProfessionalForm(forms.ModelForm):
    class Meta:
        model = RecommendProfessional
        exclude = ['created_on']