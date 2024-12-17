from pathlib import Path

from os import getenv, path
from dotenv import load_dotenv
from datetime import timedelta
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

APPS_DIR = BASE_DIR / "core_apps"

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "phonenumber_field",
    "drf_yasg",
    "djoser",
    "social_django",
    "taggit",
    "django_filters",
    "djcelery_email",

    "django_celery_beat",
    'storages',
]

LOCAL_APPS = [
    # "core_apps.issues",
    "core_apps.users",
    "core_apps.common",
    "core_apps.reading",
    "core_apps.quera",
    # "core_apps.posts",
    # "core_apps.apartments",
    # "core_apps.reports",
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
       "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_USER"),
        "PASSWORD": getenv("POSTGRES_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST"),
        "PORT": getenv("POSTGRES_PORT"),
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True

SITE_ID = 1

ADMIN_URL = "secret"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = str(BASE_DIR / 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAGGIT_CASE_INSENSITIVE = True

AUTH_USER_MODEL = "users.CustomUser"

CORS_ALLOW_ALL_ORIGINS = True

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10

CELERY_TASK_SEND_SENT_EVENT = True
CELERY_RESULT_EXTENDED = True

CELERY_RESULT_BACKEND_ALWAYS_RETRY = True

CELERY_TASK_TIME_LIMIT = 5 * 60

CELERY_TASK_SOFT_TIME_LIMIT = 60

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_WORKER_SEND_TASK_EVENTS = True

# CELERY_BEAT_SCHEDULE = {
#     "update-reputations-every-day": {
#         "task": "update_all_reputations",
#     }
# }
AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 100
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 * 48
AUTH_COOKIE_SECURE = True
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'



REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    #     "core_apps.common.cookie_auth.CookieAuthentication",
    # ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "DEFAULT_FILTER_BACKENDS": [
    #     "django_filters.rest_framework.DjangoFilterBackend",
    # ],
    # "PAGE_SIZE": 10,
    # "DEFAULT_THROTTLE_CLASSES": (
    #     "rest_framework.throttling.AnonRateThrottle",
    #     "rest_framework.throttling.UserRateThrottle",
    # ),
    # "DEFAULT_THROTTLE_RATES": {
    #     "anon": "200/day",
    #     "user": "500/day",
    # },
      # YOUR SETTINGS
  
}




SIMPLE_JWT = {
    "SIGNING_KEY": "3434hjkl34o4534523412ndfjklLlLKJSDLD",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

DJOSER = {
    "USER_ID_FIELD": "id",
    "LOGIN_FIELD": "email",
    "TOKEN_MODEL": None,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "password-reset/{uid}/{token}",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": getenv("REDIRECT_URIS", "").split(","),
    "SERIALIZERS": {
        "user_create": "core_apps.users.serializers.CreateUserSerializer",
        "current_user": "core_apps.users.serializers.CustomUserSerializer",
    },
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv("GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv("GOOGLE_CLIENT_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]

SOCIAL_AUTH_PIPELINE = [
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "core_apps.profiles.pipeline.save_profile",
]

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]


# S3 Settings


# S3 Settings Based on AWS (optional)
AWS_ACCESS_KEY_ID       = getenv("LIARA_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY   = getenv("LIARA_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = getenv("LIARA_BUCKET_NAME")
AWS_S3_ENDPOINT_URL     = getenv("LIARA_ENDPOINT")
AWS_S3_REGION_NAME      = 'us-east-1'  

# Django-storages configuration
STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}
