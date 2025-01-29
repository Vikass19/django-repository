from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    content = RichTextField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True
    )
    featured_image = models.ImageField(
        upload_to='blog_images/', null=True, blank=True
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )  # Add the author field

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)  # Reference BlogPost here
    author = models.CharField(max_length=100)  # You can also use a ForeignKey to User if you have users
    text = models.TextField()  # This field stores the comment text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class CountViews(models.Model):
    post = models.OneToOneField(BlogPost , on_delete=models.CASCADE ,  related_name= 'view_count')
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'views for  {self.post.title}'
       

class Likes(models.Model):
    post = models.ForeignKey(BlogPost , on_delete=models.CASCADE , related_name='likes')
    user = models.ForeignKey(User , on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

class Dislikes(models.Model):
    post = models.ForeignKey(BlogPost , on_delete=models.CASCADE , related_name='dislikes')
    user = models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} dislikes {self.post.title}'
    

