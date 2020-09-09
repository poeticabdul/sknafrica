from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from skn_professionals.models import ProfessionalProfile
from skn_professionals.forms import ProfessionalProfileForm, RecommendProfessionalForm

# Create your views here.



def index(request):
	if request.method == 'GET':
		try:
			professionals = ProfessionalProfile.objects.all()[:4]
		except ProfessionalProfile.DoesNotExist:
			professionals = None

		return render(request, 'index.html', {'professionals': professionals})


    # return render(request, 'find1.html')

@login_required
def profile(request):
	if request.method == 'GET':

		user = request.user
		print("type ====", user.user_type)
		if user.user_type == "Professional":

			try:
				profile = ProfessionalProfile.objects.get(user=request.user)
			except ProfessionalProfile.DoesNotExist:
				profile = None

			if profile is None:
				form = ProfessionalProfileForm()
				return render(request, 'add_profile.html', {'form': form})
				# return render(request, 'profile1.html', {'form': form})
			else:
				return render(request, 'profile.html', {'user': request.user, 'profile': profile})
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




