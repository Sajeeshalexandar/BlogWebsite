from django.contrib import admin
from .models import Category,Blogs

# Register your models here.

admin.site.register(Category)


class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('tittle',)}
    list_display = ('tittle','category','author','status','is_featured')
    search_fields =  ('id','tittle','category','author','status','is_featured')
    list_editable = ('is_featured',)

admin.site.register(Blogs,BlogsAdmin)