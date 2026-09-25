from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Blogs(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=[('Draft','Draft'),('Published','Published')])
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return self.tittle
    class Meta:
        verbose_name_plural = 'Blogs'

class About(models.Model):
    about_heading = models.CharField(max_length=100)
    about_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.about_heading
    class Meta:
        verbose_name_plural = 'About'

class Links(models.Model):
    link_name = models.CharField(max_length=25)
    link_url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
            return self.link_name
    class Meta:
        verbose_name_plural = 'Links'