from django.shortcuts import render,get_object_or_404
from .models import post as PostModel, category as CategoryModel

# Create your views here.
def posts(request):
    qs = PostModel.objects.all()
    return render(request,'blog/blog.html',{'posts':qs})

def category(request, category_id):
    category = get_object_or_404(CategoryModel ,id=category_id)
    return render(request,"blog/category.html",{'category':category})