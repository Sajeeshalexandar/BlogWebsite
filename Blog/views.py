from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog_app.models import Category,Blogs
from django.db.models import Q

def home(request):
 
    featured_post = Blogs.objects.filter(is_featured=True,status = 'Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured = False,status = 'Published').order_by('updated_at')

    context = {
    
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request,'home.html',context)

def searchBlog(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(tittle__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword),status = 'Published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)