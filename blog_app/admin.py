from django.contrib import admin
from .models import Category,Blogs,About,Links

# Register your models here.

admin.site.register(Category)


class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('tittle',)}
    list_display = ('tittle','category','author','status','is_featured')
    search_fields =  ('id','tittle','category','author','status','is_featured')
    list_editable = ('is_featured',)

admin.site.register(Blogs,BlogsAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','about_heading','about_content')
    list_editable = ('about_heading',)

admin.site.register(About,AboutAdmin)
admin.site.register(Links)