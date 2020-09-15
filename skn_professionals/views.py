from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from skn_professionals.models import ProfessionalProfile, RequesterProfile
from skn_professionals.forms import ProfessionalProfileForm, RecommendProfessionalForm, RequesterProfileForm

# Create your views here.



def index(request):
	if request.method == 'GET':

		return redirect('/accounts/signup')



@login_required
def profile(request):
	if request.method == 'GET':

		user = request.user

		print("user type is =====", user.user_type)

		if user.user_type == "Professional":

			try:
				profile = ProfessionalProfile.objects.get(user=request.user)
			except ProfessionalProfile.DoesNotExist:
				profile = None

			if profile is None:
				form = ProfessionalProfileForm()
				return render(request, 'add_profile.html', {'form': form})
			else:
				return render(request, 'profile.html', {'user': request.user, 'profile': profile})

		elif user.user_type == "Requesting Agency":
			return redirect('/find-professionals')

		else:
			return redirect('/find-professionals')
	elif request.method == 'POST':
		form = ProfessionalProfileForm(request.POST, request.FILES)
		if form.is_valid():
			pro_profile = form.save(commit=False)
			pro_profile.user = request.user
			pro_profile.save()
			return redirect('/profile')
		else:
			return render(request, 'add_profile.html', {'form': form})



@login_required
def find_professionals(request):
	if request.method == 'GET':

		if request.user.user_type == "Requesting Agency":

			try:
				profile = RequesterProfile.objects.get(user=request.user)
			except RequesterProfile.DoesNotExist:
				profile = None

			if profile is None:
				return redirect('/requester-profile')
			elif profile.admin_approved == "Yes":
				pass
			elif profile.admin_approved == "No":
				return render(request, 'not_allowed.html')


		try:
			professionals = ProfessionalProfile.objects.filter().order_by('-created_on')
		except ProfessionalProfile.DoesNotExist:
			professionals = None


		return render(request, 'find.html', {'professionals': professionals})



@login_required
def detail_of_professional(request, id_of_professional):
	if request.method == "GET":

		try:
			professional = ProfessionalProfile.objects.get(pk=id_of_professional)
		except ProfessionalProfile.DoesNotExist:
			professional = None

		return render(request, 'profile_detail.html', {'profile': professional})



@login_required
def requester_profile(request):
	if request.method == "POST":
		form = RequesterProfileForm(request.POST, request.FILES)
		if form.is_valid():

			req_profile = form.save(commit=False)
			req_profile.user = request.user
			req_profile.save()
			return render(request, 'choose_request_service.html')

		else:
			return render(request, 'add_requester_profile.html', {'form': form})
	elif request.method == "GET":
		try:
			profile = RequesterProfile.objects.get(user=request.user)
		except RequesterProfile.DoesNotExist:
			profile = None

		if profile is None:
			form = RequesterProfileForm()
			return render(request, 'add_requester_profile.html', {'form': form})
		elif profile.admin_approved == "Yes":
			return redirect('/find-professionals')
		elif profile.admin_approved == "No":
			return render(request, 'choose_request_service.html')






def recommend_professional(request):
	if request.method == 'GET':
		form = RecommendProfessionalForm()
		return render(request, 'recommend.html', {'form': form})
	elif request.method == 'POST':
		form = RecommendProfessionalForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'recommend_thankyou.html')
		else:
			return render(request, 'recommend.html', {'form': form})




