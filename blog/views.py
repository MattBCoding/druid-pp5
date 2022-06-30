from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import BlogPostForm, BlogCategoryForm
from .models import BlogPost, BlogCategory
from products.utils import paginateProducts

# Create your views here.
User = get_user_model()


def blog(request):
    '''
    View to display blog post page
    '''
    posts = BlogPost.objects.all().order_by('-created_on')
    custom_range, posts = paginateProducts(request, posts, 4)
    context = {
        'posts': posts,
        'custom_range': custom_range,
    }
    return render(request, 'blog/blog.html', context)


def blogPostDetail(request, slug):
    '''
    View to return individual blog post
    '''
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_post_detail.html', context)


@staff_member_required
def addBlogPost(request):
    '''
    View to handle displaying add blog form
    and to handle form processing
    '''
    form = BlogPostForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Blog Post successfully added!')
            return redirect('blog')
        else:
            messages.error(
                request,
                'Failed to add the blog post, \
                    please ensure the form is correctly filled in'
                )
    return render(request, 'blog/blog_post_form.html', context)


@staff_member_required
def editBlogPost(request, slug):
    '''
    View to display prefilled form to edit a blog post
    and to handle form processing
    '''
    post = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(instance=post)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.author = request.user
            edited_form.save()
            messages.success(request, 'Blog Post successfully updated!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update blog post, \
                please double check the form.')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'blog/blog_post_form.html', context)


@staff_member_required
def deleteBlogPost(request, pk):
    '''
    View to handle the deletion of a blog post
    '''
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user.is_staff:
        post.delete()
        messages.success(request, 'The post has been deleted.')
        return redirect('blog')
    else:
        messages.error(request, 'Only employees can delete blog posts.')


@staff_member_required
def getCategories(request):
    '''
    View to return categorie
    '''
    categories = BlogCategory.objects.all()
    context = {
        'categories': categories,
        'disabled': False,
    }

    return render(request, 'blog/snippets/categories.html', context)


@staff_member_required
def addBlogCategory(request):
    '''
    View to display form to add a blog post category
    and to handle form processing
    '''
    form = BlogCategoryForm()
    context = {
        'category_form': form,
        'disabled': True,
    }

    if request.htmx:
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            name = form.cleaned_data['name']
            form.save()
            category = BlogCategory.objects.get(name=name)
            context = {
                'category': category,
                'disabled': False,
            }
            return render(
                          request,
                          'blog/snippets/add_blog_category_container.html',
                          context)

    return render(request, 'blog/snippets/add_category_form.html', context)


@staff_member_required
def getAddBlogCategoryContainer(request):
    '''
    View to handle inserting container for future requests
    '''
    return render(request, 'blog/snippets/add_blog_category_container.html')


@staff_member_required
def editBlogCategory(request, pk):
    '''
    View to display prefilled blog category form
    and to handle form processing
    '''
    category = BlogCategory.objects.get(pk=pk)
    form = BlogCategoryForm(instance=category)
    context = {
        'category_form': form,
        'category': category,
    }
    if request.htmx:
        form = BlogCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            category.refresh_from_db()
            context = {
                'category': category,
            }
            return render(
                          request,
                          'blog/snippets/category_detail.html',
                          context)

    return render(request, 'blog/snippets/category_form.html', context)


@staff_member_required
def getBlogCategoryDetail(request, pk):
    '''
    View to return category details
    '''
    category = BlogCategory.objects.get(pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'blog/snippets/category_detail.html', context)


@staff_member_required
def getDeleteBlogCategory(request, pk):
    '''
    View to provide option for deleting a blog category
    '''
    category = BlogCategory.objects.get(pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'blog/snippets/category_delete.html', context)


@staff_member_required
def deleteBlogCategory(request, pk):
    '''
    View to handle deleting blog categories
    prevents deletion of the general category
    '''
    if pk != '1':
        category = BlogCategory.objects.get(pk=pk)
        name = category.name
        category.delete()
        context = {
            'name': name,
        }
        return render(
                      request,
                      'blog/snippets/category_delete_response.html',
                      context)

    else:
        messages.error(request, "Error - Administrator needed to \
            delete the default category.")
        posts = BlogPost.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'blog/blog.html', context)
