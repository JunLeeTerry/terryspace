from django.shortcuts import render_to_response
from terryspace.blog.models import Article,Author,Classification
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return __paginatorObject(request,blogs)

def blog_eclipse(request):
    eclipse_blogs = Article.objects.filter(classification__name='Eclipse').order_by('-publish_time')
    return __paginatorObject(request,eclipse_blogs)

def blog_python(request):
    python_blogs = Article.objects.filter(classification__name='Python').order_by('-publish_time')
    return __paginatorObject(request,python_blogs)
    

def blog_java(request):
    java_blogs = Article.objects.filter(classification__name='Java').order_by('-publish_time')
    return __paginatorObject(request,java_blogs)
    
def blog_life(request):
    life_blogs = Article.objects.filter(classification__name='Life').order_by('-publish_time')
    return __paginatorObject(request,life_blogs)
    
def __paginatorObject(request,blogs):
    page_size=5
    after_range_num = 5
    before_range_num = 6   
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1  
    paginator = Paginator(blogs,page_size)
    try:
        blogs = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        blogs = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
    return render_to_response("blogs.html",{"page_objects":blogs,"page_range":page_range})
