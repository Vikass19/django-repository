from .views import *
from django.urls import path

urlpatterns = [
     # path('api/categories/', CategoryListView.as_view(), name='category-list'),
      path('api/subscribe/', NewsletterSubscriptionView.as_view(), name='newsletter-subscribe'),
     
     ]
