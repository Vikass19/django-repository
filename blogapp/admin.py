from django.contrib import admin
from django.contrib.auth.models import User
from .models import BlogPost, Category, Comment, UserProfile , Subscription
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.admin.models import LogEntry

# Register UserProfile
admin.site.register(UserProfile)
admin.site.register(Subscription)

# Unregister the default User model admin
admin.site.unregister(User)

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Create a custom form for BlogPost
class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    content = forms.CharField(widget=CKEditorWidget())

# Register BlogPost model with custom admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        queryset.update(status='published')

    mark_as_published.short_description = "Mark selected blog posts as published"

admin.site.register(BlogPost, BlogPostAdmin)

# Register Comment model
admin.site.register(Comment)

# Register LogEntry model
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_time', 'content_type', 'object_repr', 'action_flag')
    search_fields = ['user__username']

admin.site.register(LogEntry, LogEntryAdmin)

# Optionally, register User with custom admin
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # You can customize the User admin here if needed
    pass

admin.site.register(User, CustomUserAdmin)
