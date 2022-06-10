from django.shortcuts import render
from .forms import BlogPostForm, BlogCategoryForm
from .models import BlogPost

# Create your views here.
def blog(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)