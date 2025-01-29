from .models import BlogPost , Comment , Category , Likes , Dislikes
from rest_framework import serializers
from .models import User , UserProfile



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'photo']  # Add 'photo' to the serialized fields

class BlogPostSerializer(serializers.ModelSerializer):
    views = serializers.IntegerField(source = 'view_count.count' , read_only = True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id' , 'title' , 'content' , 'created_at' ,'featured_image' , 'slug' , 'views' , 'likes_count' , 'dislikes_count' ]

        
    def get_likes_count(self, obj):
        return obj.likes.count()
        
    def get_dislikes_count(self ,obj):
            return obj.dislikes.count()
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id' , 'post' , 'user']

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislikes
        fields = ['id' , 'post' , 'user'  ]              




class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']

    # Optional: Define custom validation for text
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment text cannot be empty")
        return value

    def validate_post(self, value):
        if not value:
            raise serializers.ValidationError("Post must be provided")
        return value
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'picture']