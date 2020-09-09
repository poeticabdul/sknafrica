# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class User(AbstractUser):

    USER_TYPE = (
        ('Professional', 'Professional'),
        ('Partner', 'Partner'),
        ('Other', 'Other'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPE, default="Professional")



class ProfessionalProfile(models.Model):

	FIELD_OF_EXPERTISE = (
        ('Agriculture', 'Agriculture'),
        ('Business/Commerce & Industry', 'Business/Commerce & Industry'),
        ('Communications, Media, IT', 'Communications, Media, IT'),
        ('Criminology & Criminal Justice', 'Criminology & Criminal Justice'),
        ('Culture & Heritage', 'Culture & Heritage'),
        ('Development and International Development', 'Development and International Development'),
        ('Diplomacy and International Relations', 'Diplomacy and International Relations'),
        ('Economy', 'Economy'),
        ('Education', 'Education'),
        ('Elections', 'Elections'),
        ('Energy', 'Energy'),
        ('Employment', 'Employment'),
        ('Finance, Banking, Microfinance', 'Finance, Banking, Microfinance'),
        ('Fiscal Policy', 'Fiscal Policy'),
        ('Government & Politics', 'Government & Politics'),
        ('Health', 'Health'),
        ('History of Ghana', 'History of Ghana'),
        ('Humanities', 'Humanities'),
        ('Infrastructure & Planning', 'Infrastructure & Planning'),
        ('Law/Legal', 'Law/Legal'),
        ('Linguistics/Language', 'Linguistics/Language'),
        ('Public Service & Public Administration', 'Public Service & Public Administration'),
        ('Security & Defense', 'Security & Defense'),
        ('Social Sciences', 'Social Sciences'),
        ('Science & STEM', 'Science & STEM'),
        ('Social Justice, Gender, Youth & Diversity', 'Social Justice, Gender, Youth & Diversity'),
        ('Sports', 'Sports'),
        ('Violence Against Women', 'Violence Against Women'),
        ('Women and Politics', 'Women and Politics'),
        ('Women in Media', 'Women in Media'),
        ('Other', 'Other'),
    )

	LEVEL_OF_EXPERTISE = (
		('Early Career: 3-6 Years', 'Early Career: 3-6 Years'),
		('Mid Career: 7-12 Years', 'Mid Career: 7-12 Years'),
		('Experienced: 12+ Years', 'Experienced 12+ Years'),
	)

	DISCOVER_SKN = (
		('Friends & Family', 'Friends & Family'),
		('Social Media', 'Social Media'),
		('Publications', 'Publications'),
		('TV', 'TV'),
		('Radio', 'Radio'),
		('Other', 'Other'),
	)

	CERTIFY_ACCOUNT = (
		('Yes', 'Yes'),
		('No', 'No'),
	)

	APPROVED = (
		('Yes', 'Yes'),
		('No', 'No'),
	)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

	
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	phone_number = models.CharField(validators=[phone_regex], max_length=15)
	country_of_residence = CountryField(blank_label='(Select Country)')
	nationality = CountryField(blank_label='(Select Country)', blank=True, null=True)
	town_or_city_of_residence = models.CharField(max_length=150, blank=True, null=True)
	field_of_expertise = models.CharField(max_length=60, choices=FIELD_OF_EXPERTISE)
	level_of_expertise = models.CharField(max_length=30, choices=LEVEL_OF_EXPERTISE)
	job_title = models.CharField(max_length=60)
	job_description = models.TextField()
	link_to_social_media_handle = models.CharField(max_length=150, blank=True, null=True)
	languages_spoken = models.CharField(max_length=100, blank=True, null=True)
	profile = models.TextField()
	certify_account = models.CharField(max_length=10, choices=CERTIFY_ACCOUNT)
	cv_resume = models.FileField()
	assistant_name = models.CharField(max_length=45, blank=True, null=True)
	assistant_phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
	assistant_email = models.EmailField(max_length=250, blank=True, null=True)
	referee_one_full_name = models.CharField(max_length=60)
	referee_one_phone_number = models.CharField(validators=[phone_regex], max_length=15)
	referee_one_email = models.EmailField(max_length=150)
	referee_one_workplace = models.CharField(max_length=60)
	referee_two_full_name = models.CharField(max_length=60)
	referee_two_phone_number = models.CharField(validators=[phone_regex], max_length=15)
	referee_two_email = models.EmailField(max_length=150)
	referee_two_workplace = models.CharField(max_length=60)
	how_did_you_discover_skn = models.CharField(max_length=20, choices=DISCOVER_SKN, default="Other")
	photo = models.ImageField(blank=True, null=True)
	terms_and_conditions_confirmed = models.BooleanField()
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	admin_approved = models.CharField(max_length=5, choices=APPROVED, default="No")
	created_on = models.DateTimeField(auto_now_add=True)
    

	def __unicode__(self):
		return self.first_name



class RecommendProfessional(models.Model):

	TITLE = (
		('Professor', 'Professor'),
		('Dr', 'Dr'),
		('Mr', 'Mr'),
		('Ms', 'Ms'),
		('Other', 'Other'),
	)

	INFORM_PROFESSIONAL = (
		('Yes', 'Yes'),
		('No', 'No'),
	)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

	
	title_of_recommender = models.CharField(max_length=10, choices=TITLE)
	recommender_first_name = models.CharField(max_length=45)
	recommender_last_name = models.CharField(max_length=45)
	recommender_email = models.EmailField(max_length=150)
	recommender_phone_number = models.CharField(validators=[phone_regex], max_length=15)
	let_professional_know = models.CharField(max_length=10, choices=INFORM_PROFESSIONAL)

	title_of_professional = models.CharField(max_length=10, choices=TITLE)
	professional_full_name = models.CharField(max_length=150)
	professional_phone_number = models.CharField(validators=[phone_regex], max_length=15)
	professional_email = models.EmailField(max_length=150)
	professional_expertise = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

    

	def __unicode__(self):
		return self.professional_full_name