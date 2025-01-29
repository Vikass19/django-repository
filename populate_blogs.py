import os
import random
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
from blogapp.models import BlogPost, Category
import requests  # Ensure you have installed requests: pip install requests

# Ensure Django environment is set up
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

def populate_blogs():
    # Check if the admin user exists; create if not
    user = User.objects.first()
    if not user:
        print("No users found. Please create at least one user before running this script.")
        return

    # Ensure some categories exist
    categories = Category.objects.all()
    if not categories.exists():
        print("No categories found. Creating default categories...")
        categories = [
            Category(name="Technology", slug="technology"),
            Category(name="Lifestyle", slug="lifestyle"),
            Category(name="Education", slug="education"),
        ]
        Category.objects.bulk_create(categories)
        categories = Category.objects.all()

    # Dummy blog post content and links
    sample_titles = [
        "Introduction to Python",
        "How to Use Django for Web Development",
        "Understanding Machine Learning",
        "Top 10 Tech Trends in 2025",
        "Building Responsive Websites",
    ]
    sample_content = """
    This is a sample blog post generated for testing purposes. You can update the content later.
    Check out [this link](https://example.com) for more information!
    """
    sample_image_url = "https://via.placeholder.com/800x400.png?text=Sample+Image"

    # Create 50 blog posts
    for i in range(1, 51):
        title = f"{random.choice(sample_titles)} #{i}"
        slug = slugify(title)
        category = random.choice(categories)
        status = random.choice(["draft", "published"])
        
        # Create the blog post
        blog = BlogPost(
            title=title,
            slug=slug,
            content=sample_content,
            category=category,
            status=status,
            author=user,
            created_at=now(),
            updated_at=now(),
        )
        # Save the blog to assign an ID
        blog.save()

        # Add an image
        response = requests.get(sample_image_url)
        if response.status_code == 200:
            file_name = f"blog_image_{i}.png"
            blog.featured_image.save(file_name, ContentFile(response.content))

        print(f"Created blog post: {title}")

    print("Successfully created 50 blog posts.")

if __name__ == "__main__":
    populate_blogs()
