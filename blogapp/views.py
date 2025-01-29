from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import BlogPost, Comment, Category, UserProfile, Subscription
from .serializers import (
    BlogPostSerializer, CommentSerializer, CategorySerializer, UserProfileSerializer
)
from django.contrib.auth.models import User

# BlogPost ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Increment the views count for a specific blog post."""
        post = self.get_object()
        post.views += 1
        post.save()
        return Response({'views': post.views}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """Handle like functionality for a blog post."""
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            message = "Like removed"
        else:
            post.likes.add(user)
            post.dislikes.remove(user)
            message = "Liked successfully"
        return Response({'likes_count': post.likes.count(), 'message': message}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def dislike(self, request, pk=None):
        """Handle dislike functionality for a blog post."""
        post = self.get_object()
        user = request.user
        if user in post.dislikes.all():
            post.dislikes.remove(user)
            message = "Dislike removed"
        else:
            post.dislikes.add(user)
            post.likes.remove(user)
            message = "Disliked successfully"
        return Response({'dislikes_count': post.dislikes.count(), 'message': message}, status=status.HTTP_200_OK)

# UserProfile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Optionally restricts the returned profiles to the currently authenticated user."""
        user = self.request.user
        if user.is_authenticated:
            return UserProfile.objects.filter(user=user)
        return UserProfile.objects.none()

    def create(self, request, *args, **kwargs):
        """Create a new user profile."""
        user_data = request.data
        user, created = User.objects.get_or_create(email=user_data['email'])
        user_profile, _ = UserProfile.objects.get_or_create(user=user)
        user_profile.name = user_data.get('name', '')
        user_profile.picture = user_data.get('picture', '')
        user_profile.save()
        return Response({'message': 'User data saved successfully.'}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Update an existing user profile."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Filter comments by post ID."""
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def create(self, request, *args, **kwargs):
        """Create a new comment."""
        post_id = request.data.get('post')
        if not post_id:
            return Response({"error": "post_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        post = get_object_or_404(BlogPost, id=post_id)
        author = request.data.get('author') or request.user.username
        text = request.data.get('text')
        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(post=post, author=author, text=text)
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Newsletter Subscription View
class NewsletterSubscriptionView(APIView):
    def post(self, request):
        """Handle newsletter subscription."""
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        if Subscription.objects.filter(email=email).exists():
            return Response({'message': 'Already subscribed'}, status=status.HTTP_200_OK)

        Subscription.objects.create(email=email)
        return Response({'message': 'Subscription successful'}, status=status.HTTP_201_CREATED)
