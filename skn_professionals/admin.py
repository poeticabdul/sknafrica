from django.contrib import admin

# Register your models here.

from skn_professionals.models import ProfessionalProfile, RecommendProfessional

class ProfessionalProfileAdmin(admin.ModelAdmin):

	search_fields = ['first_name', 'last_name']
	list_display = ('first_name', 'last_name', 'phone_number', 'certify_account', 'admin_approved')


class RecommendProfessionalAdmin(admin.ModelAdmin):

	search_fields = ['recommender_first_name', 'professional_full_name']
	list_display = ('title_of_professional', 'professional_full_name', 'professional_email', 'professional_phone_number', 'recommender_first_name')


admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)
admin.site.register(RecommendProfessional, RecommendProfessionalAdmin)
