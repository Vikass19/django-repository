
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blogapp.views import PostViewSet , CommentViewSet , UserProfileViewSet , CategoryViewSet

router = DefaultRouter()
router.register(r'posts' , PostViewSet)
router.register(r'comments', CommentViewSet)  #  this line to register the CommentViewSet
router.register(r'user-profile', UserProfileViewSet, basename='user-profile')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blogapp.urls')),
    path('api/' , include(router.urls)),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
 

