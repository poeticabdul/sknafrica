from django.contrib import admin

# Register your models here.

from skn_professionals.models import ProfessionalProfile, RequesterProfile, RecommendProfessional

class ProfessionalProfileAdmin(admin.ModelAdmin):

	search_fields = ['first_name', 'last_name']
	list_display = ('first_name', 'last_name', 'phone_number', 'certify_account', 'admin_approved')



class RequesterProfileAdmin(admin.ModelAdmin):
	search_fields = ['requester_full_name', 'requester_organization']
	list_display = ('requester_full_name', 'requester_organization', 'requester_phone_number')



class RecommendProfessionalAdmin(admin.ModelAdmin):

	search_fields = ['recommender_first_name', 'professional_full_name']
	list_display = ('title_of_professional', 'professional_full_name', 'professional_email', 'professional_phone_number', 'recommender_first_name')


admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)
admin.site.register(RequesterProfile, RequesterProfileAdmin)
admin.site.register(RecommendProfessional, RecommendProfessionalAdmin)
