from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xiiu+0^6x+1frzg4$3i4@98bsf5g28meu4ji^d9^ubdqfx$et#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    

    'corsheaders',
    'rest_framework',
    'blogapp',  # Your custom app
    'ckeditor',
    
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Correct placement for custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'auth.User'

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# settings.py
APPEND_SLASH = False

# Ensure static files are collected
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
# For production, you may need to run collectstatic
# python manage.py collectstatic

# Media files (uploaded images, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Ensure it's properly joined with `Path`

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#allowed specific origins
CORS_ALLOWED_ORIGINS = [
     "http://localhost:5173",  
    "http://127.0.0.1:8000",
    "https://frontendrepo-iikg.vercel.app",  # Added frontend URL here
     # React frontend URL
    
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True


ALLOWED_HOSTS = ['*']


JAZZMIN_SETTINGS = {
    # Title and header in the admin panel
    'site_title': 'My Blog Website',
    'site_header': 'Admin Dashboard',
    'site_brand': 'fixerror29',

    # Custom CSS and JS if needed
    'custom_css': 'css/custom_admin.css',  # Create a custom CSS file for more styling
    'custom_js': 'js/custom_admin.js',     # Optional JS for extra features

    # Change the color scheme (optional)
    'primary_color': '#0d6efd',  # Set primary color to blue

    # Sidebar settings
    'show_sidebar': True,  # Show or hide sidebar
    'sidebar_max_width': '250px',  # Set max width of the sidebar

    # Models and app configuration (optional)
    'changeform_format': 'vertical',  # Vertical form layout for model forms

    # Grouping model list (optional)
    'navigation_expanded': True,  # Automatically expand the navigation menu

    # Other configurations
    'topmenu_links': [
        {'name': 'Home', 'url': '/admin', 'permissions': ['auth.view_user']},
        {'name': 'Docs', 'url': 'https://docs.djangoproject.com/en/stable/', 'new_window': True},
    ],
}


JAZZMIN_SETTINGS = {
    'icon_size': 'lg',  # Icon size can be small, medium, or large
    'icons': {
        'auth': 'fas fa-user',  # FontAwesome icons for apps
        'myapp': 'fas fa-cogs',
    },
}


