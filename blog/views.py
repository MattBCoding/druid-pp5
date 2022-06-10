from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import BlogPostForm, BlogCategoryForm
from .models import BlogPost

# Create your views here.
User = get_user_model()

def blog(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)

@login_required
def addBlogPost(request, pk):
    form = BlogPostForm()
    profile = get_object_or_404(User, pk=pk)
    context = {
        'form': form,
        'profile': profile,
    }
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.author = profile.id
            form.save()
            messages.success(request, 'Blog Post successfully added!')
            return redirect('blog')
        else:
            messages.error(
                request,
                'Failed to add the blog post, please ensure the form is correctly filled in'
                )
    return render(request, 'blog/add_blog_post.html', context)