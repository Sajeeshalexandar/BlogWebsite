from .models import Category,About,Links

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)
def get_about(request):
    about = About.objects.get()
    return dict(about = about)
def get_links(request):
    links = Links.objects.all()
    return dict(links = links)