"""sheknowsnetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from skn_professionals.views import index, profile, find_professionals, detail_of_professional, recommend_professional
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', index, name='index'),
	path('profile', profile, name='profile'),
	path('find-professionals', find_professionals, name='find_professionals'),
    path('recommend-professional', recommend_professional, name='recommend_professional'),
    path('p/<int:id_of_professional>/', detail_of_professional, name='detail_of_professional'),
	path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

