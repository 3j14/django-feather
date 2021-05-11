import os


BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django_feather",
)

SECRET_KEY = "django-feather-test"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

MIDDLEWARE_CLASSES = ("django.middleware.common.CommonMiddleware",)

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": True,
        },
    },
]
