from django import forms
from skn_professionals.models import ProfessionalProfile, RequesterProfile, RecommendProfessional


class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        exclude = ['user', 'nationality', 'created_on', 'admin_approved']



class RequesterProfileForm(forms.ModelForm):
    class Meta:
        model = RequesterProfile
        exclude = ['user', 'created_on', 'admin_approved']

    def clean(self):
        cleaned_data = super().clean()
        requester_photo_id = cleaned_data.get("requester_photo_id")
        referee_one_email = cleaned_data.get("referee_one_email")

        if not requester_photo_id and not referee_one_email:
        	raise forms.ValidationError("You need to provide a photo id or referees.")



class RecommendProfessionalForm(forms.ModelForm):
    class Meta:
        model = RecommendProfessional
        exclude = ['created_on']