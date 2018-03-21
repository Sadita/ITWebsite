"""
Django settings for scotDives project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths for templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Build paths for static files
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Build paths for media files
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yvmiz0carwiauwds4$7)brr2e*pm)fo&g&9o_+s27@t(hn706)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['scotdives.pythonanywhere.com',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scotDives',
    'django.contrib.sites',
    
	#django-social-login
    'social.apps.django_app.default',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'itWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',  
            ],
        },
    },
]


WSGI_APPLICATION = 'itWebsite.wsgi.application'

# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': { 'min_length': 6, }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)

# If True, users can register
REGISTRATION_OPEN = True
# One-week activation window; you may, of course, use a different value.
ACCOUNT_ACTIVATION_DAYS = 7
# If True, the user will be automatically logged in.
REGISTRATION_AUTO_LOGIN = True
# The page you want users to arrive at after they successfully log in
LOGIN_REDIRECT_URL = 'index'
# The page users are directed to if they are not logged in,
# and are trying to access pages requiring authentication
#LOGIN_URL = '/accounts/login/'
LOGIN_URL = '/scot-dives/login/'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]
STATIC_ROOT = os.path.join('/home/scotDives/ITWebsite/staticroot/')
# Variables to set up media file hosting
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

SITE_ID = 1

#SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#SESSION_COOKIE_AGE = 1209600

#-----(social login start)-----

AUTHENTICATION_BACKENDS = (
    #'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    #'social.backends.twitter.TwitterOAuth',
	
	'social_core.backends.twitter.TwitterOAuth',

    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

#facebook login
SOCIAL_AUTH_FACEBOOK_KEY = '142678796553745'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '0df8808d9979b1fe72d4aa5e29bd2b33'    # App Secret
SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = 'scotdives'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {

  'fields': 'id, name, email'

}
# SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'

#twitter login
SOCIAL_AUTH_TWITTER_KEY = 'd7GqghPSipnSQIkmkDTk2XIkL'
SOCIAL_AUTH_TWITTER_SECRET = 'VFlmSAC0hd3M3EnXbkzzFvEzZjT1Lua9MPLwU1LE7xhHAa06Z8'

SOCIAL_AUTH_TWITTER_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

#13mar
#SOCIAL_AUTH_LOGIN_ERROR_URL = '/scot-dives/settings/'
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/scot-dives/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
