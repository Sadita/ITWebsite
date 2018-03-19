"""itWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from scotDives import views
from registration.backends.simple.views import RegistrationView
from scotDives.forms import UserForm

# Create a new class that redirects the user to the index page, #if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/scot-dives/profile_registration/'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'scot-dives/', include('scotDives.urls')),
    # above maps any URLs starting
    # with scot-dives/ to be handled by
    # the scotDives application
    url(r'^admin/', admin.site.urls),
    url(r'^scot-dives/register/$', MyRegistrationView.as_view(form_class=UserForm), name='registration_register'),
    url(r'^scot-dives/', include('registration.backends.simple.urls')),

    #--social-login--
    url('', include('social.apps.django_app.urls', namespace='social')),	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

