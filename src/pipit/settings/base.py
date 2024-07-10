from datetime import timedelta
import os
from typing import Optional

from utils.env import get_env, get_env_bool  # NOQA: F401


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Version, be sure to bump this with each release (please follow semver.org)
APP_VERSION = "0.1.0"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env("SECRET_KEY", required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# This is when debug is off, else django wont allow you to visit the site
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS", required=True).split(",")

# INTERNAL_IPS = ["127.0.0.1"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.flatpages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.gis",
    'django.contrib.sites',
    # Third party apps
    'wagtail_content_import',
    "wagtail_content_import.pickers.local",
    'wagtail_content_import.pickers.microsoft',
    'wagtail_content_import.pickers.google',
    "dashboard",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.admin",
    "wagtail",
    "wagtail.search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "modelcluster",
    "taggit",
    "wagtail_meta_preview",
    "wagtail_headless_preview",
    "rest_framework",
    'rest_framework_simplejwt',
    "drf_yasg",
    "corsheaders",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.google',
    "wagtailmarkdown",

    # Project specific apps
    "pipit",
    "sitesettings",
    "customuser",
    "customimage",
    "customdocument",
    "main",
    "nextjs",
    "jobs",
]

WAGTAILAPI_LIMIT_MAX= 20 

# CORS_ALLOWED_ORIGINS = [ "*",
#     # 'http://localhost:3000',
#     # 'http://127.0.0.1:3000',
# ]

#Social Auth
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "pipit.urls"
APPEND_SLASH = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",

                # Project specific
                "pipit.context_processors.settings_context_processor",
            ],
        },
    }
]



WSGI_APPLICATION = "pipit.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# Using PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": get_env("DATABASE_NAME", required=True),
        "USER": get_env("DATABASE_USER", required=True),
        "PASSWORD": get_env("DATABASE_PASSWORD", required=True),
        "HOST": get_env("DATABASE_HOST", required=True),
        "PORT": int(get_env("DATABASE_PORT", default="5432")),
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 'rest_framework.authentication.TokenAuthentication',
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "EXCEPTION_HANDLER": "jobs.api.custom_exception.custom_exception_handler",
}



SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "customuser.api.custom_clains.MyTokenObtainPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Documentation
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}},
    "DEFAULT_FIELD_INSPECTORS": [
        "drf_yasg.inspectors.CamelCaseJSONFilter",
        "drf_yasg.inspectors.InlineSerializerInspector",
        "drf_yasg.inspectors.RelatedFieldInspector",
        "drf_yasg.inspectors.ChoiceFieldInspector",
        "drf_yasg.inspectors.FileFieldInspector",
        "drf_yasg.inspectors.DictFieldInspector",
        "drf_yasg.inspectors.SimpleFieldInspector",
        "drf_yasg.inspectors.StringDefaultFieldInspector",
    ],
    "USE_SESSION_AUTH": False,
}

AUTHENTICATION_BACKENDS = (
    # "social_core.backends.github.GithubOAuth2",
    # "social_core.backends.twitter.TwitterOAuth",
    # "social_core.backends.facebook.FacebookOAuth2",
    # "social_core.backends.linkedin.LinkedinOAuth2",
    # "social_core.backends.google.GoogleOAuth2",
    # "graphql_jwt.backends.JSONWebTokenBackend",
    # 'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # NOQA
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},  # NOQA
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},  # NOQA
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"  # NOQA
    },
]

SITE_ID = 1  # new

ACCOUNT_EMAIL_VERIFICATION = "none"  # new

# LOGIN_REDIRECT_URL = "/"  # new

SOCIALACCOUNT_PROVIDERS = {
    # 'facebook': {
    #     'METHOD': 'oauth2',
    #     'SCOPE': ['email', 'public_profile', 'user_friends'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'email',
    #         'name',
    #         'first_name',
    #         'last_name',
    #         'verified',
    #         'locale',
    #         'timezone',
    #         'link',
    #         'gender',
    #         'updated_time',
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC': 'path.to.callable',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v2.12',
    # },
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
TIME_ZONE = "Europe/Stockholm"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Email
DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL", default="noreply@example.com")

# Auth
AUTH_USER_MODEL = "customuser.User"

# Wagtail
WAGTAIL_SITE_NAME = "Company-Project"
WAGTAILIMAGES_IMAGE_MODEL = "customimage.CustomImage"
WAGTAILDOCS_DOCUMENT_MODEL = "customdocument.CustomDocument"
WAGTAIL_ALLOW_UNICODE_SLUGS = False

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

WAGTAILMARKDOWN = {
    "autodownload_fontawesome": True,
    "allowed_tags": [],  # optional. a list of HTML tags. e.g. ['div', 'p', 'a']
    "allowed_styles": [],  # optional. a list of styles
    "allowed_attributes": {},  # optional. a dict with HTML tag as key and a list of attributes as value
    "allowed_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
    "extensions": [],  # optional. a list of python-markdown supported extensions
    "extension_configs": {},  # optional. a dictionary with the extension name as key, and its configuration as value
    "extensions_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
    "tab_length": 4,  # optional. Sets the length of tabs used by python-markdown to render the output. This is the number of spaces used to replace with a tab character. Defaults to 4.
}

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    "png": "jpeg",
    "webp": "webp",
}

# Uploaded media
# MEDIA_URL = "/wt/media/"
# MEDIA_ROOT = get_env("MEDIA_PATH", required=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = "/wt/static/"

# The absolute path to the directory where collectstatic will collect static
# files for deployment. Example: "/var/www/example.com/static/"I
STATIC_ROOT = get_env("STATIC_PATH", required=True)

# This setting defines the additional locations the staticfiles will traverse
STATICFILES_DIRS = (
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
)

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Admin
ADMIN_URL = "wt/admin/"

# NextJS
WAGTAIL_HEADLESS_PREVIEW = {
    "CLIENT_URLS": {
        "default": "/api/preview/",
    }
}

# SOCIAL_AUTH_GITHUB_KEY = env("SOCIAL_AUTH_GITHUB_KEY", default="")
# SOCIAL_AUTH_GITHUB_SECRET = env("SOCIAL_AUTH_GITHUB_SECRET", default="")

# SOCIAL_AUTH_FACEBOOK_KEY = env("SOCIAL_AUTH_FACEBOOK_KEY", default="")
# SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET", default="")

# SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "id, name, email, age_range"}

# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = env("SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY", default="")
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = env("SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET", default="")

# SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ["r_liteprofile", "r_emailaddress"]
# SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ["emailAddress"]

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", default="")
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", default="")

# SOCIAL_AUTH_PIPELINE = (
#     "social_core.pipeline.social_auth.social_details",
#     "social_core.pipeline.social_auth.social_uid",
#     "social_core.pipeline.social_auth.auth_allowed",
#     "social_core.pipeline.social_auth.social_user",
#     "social_core.pipeline.user.get_username",
#     "social_core.pipeline.user.create_user",
#     "social_core.pipeline.social_auth.associate_user",
#     "social_core.pipeline.social_auth.load_extra_data",
#     "social_core.pipeline.user.user_details",
#     "accounts.pipeline.update_user",
# )

# Sentry
SENTRY_DSN: Optional[str] = None
SENTRY_ENVIRONMENT: Optional[str] = None

if get_env("AWS_STORAGE_BUCKET_NAME"):
    # Add django-storages to the installed apps
    INSTALLED_APPS = INSTALLED_APPS + ["storages"]

    # https://docs.djangoproject.com/en/stable/ref/settings/#default-file-storage
    
    STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": get_env("AWS_ACCESS_KEY_ID"),
            "secret_key": get_env("AWS_SECRET_ACCESS_KEY"),
            "bucket_name": get_env("AWS_STORAGE_BUCKET_NAME"),
            "region_name": get_env("AWS_LOCATION"),
            "custom_domain": get_env("AWS_S3_CUSTOM_DOMAIN"),
  
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": get_env("AWS_ACCESS_KEY_ID"),
            "secret_key": get_env("AWS_SECRET_ACCESS_KEY"),
            "bucket_name": get_env("AWS_STORAGE_BUCKET_NAME"),
            "region_name": get_env("AWS_LOCATION"),
            "custom_domain": get_env("AWS_S3_CUSTOM_DOMAIN"),
        },
    },
    
}
    # print(get_env("AWS_STORAGE_BUCKET_NAME"), get_env("AWS_ACCESS_KEY_ID"), get_env("AWS_SECRET_ACCESS_KEY"), get_env("AWS_LOCATION"), get_env("AWS_S3_CUSTOM_DOMAIN"))
    AWS_S3_CUSTOM_DOMAIN = get_env("AWS_S3_CUSTOM_DOMAIN")
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    # Disables signing of the S3 objects' URLs. When set to True it
    # will append authorization querystring to each URL.
    AWS_QUERYSTRING_AUTH = False

    # Do not allow overriding files on S3 as per Wagtail docs recommendation:
    # https://docs.wagtail.io/en/stable/advanced_topics/deploying.html#cloud-storage
    # Not having this setting may have consequences in losing files.
    AWS_S3_FILE_OVERWRITE = False

    # Default ACL for new files should be "private" - not accessible to the
    # public. Images should be made available to public via the bucket policy,
    # where the documents should use wagtail-storages.
    AWS_DEFAULT_ACL = "private"