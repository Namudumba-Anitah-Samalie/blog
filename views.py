from django.shortcuts import render
import random

# Global lists (all from the same person)
blogs = [
    "Attending my first Django web app was exciting and amazing!",
    "It is easy and exciting to learn how to link URLs, Views, and Templates in Django.",
    "Exploring how Python powers web development efficiently is a task worth undertaking."
]

# Image URLs (stored in static folder)
images = [
    "django1.png",
    "django2.png",
    "django3.png"
]

# Home page view (/) - shows random blog & image
def base(request):
    selected_blog = random.choice(blogs)
    selected_image = random.choice(images)
    context = {
        'blog': selected_blog,
        'image': selected_image
    }
    return render(request, 'base.html', context)

# Blog page view (/blog/) - also random blog & image
def blog(request):
    selected_blog = random.choice(blogs)
    selected_image = random.choice(images)
    context = {
        'blog': selected_blog,
        'image': selected_image
    }
    return render(request, 'blog.html', context)

# Show all blogs and images
def show_all(request):
    context = {
        'blogs': blogs,
        'images': images
    }
    return render(request, 'show_all.html', context)

# About page view
def about(request):
    context = {
        'name': 'ANITAH SAMALIE',
        'bio': 'I am excited about being a Django enthusiast learning web development. This app displays my blogs and visuals.'
    }
    return render(request, 'about.html', context)

