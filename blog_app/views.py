from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Blogs,Category

# Create your views here.

def post_by_category(request,category_id):
    blog_post = Blogs.objects.filter(category = category_id,status = 'Published')
    category = Category.objects.get(id = category_id)
    context = {
        'blog_post':blog_post,
        'category':category
    }
    return render(request,'category_post.html',context)

def single_page(request,slug):
    post = get_object_or_404(Blogs, slug = slug ,status = "Published")
    context = {
        'post': post
    }
    return render(request,'single_page.html',context)