from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    USER_TYPE = (
        ('Professional', 'Professional'),
        ('Partner', 'Partner'),
        ('Other', 'Other'),
    )
    user_type = forms.CharField(widget=forms.Select(choices=USER_TYPE))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user