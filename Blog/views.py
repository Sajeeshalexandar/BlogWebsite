from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog_app.models import Category,Blogs


def home(request):
 
    featured_post = Blogs.objects.filter(is_featured=True,status = 'Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured = False,status = 'Published').order_by('updated_at')

    context = {
    
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request,'home.html',context)

