from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

# def index(request):
#     posts=Post.objects.all().order_by('-pk')  #최신 글부터 배치
#     return render(request, 'blog/index.html', {'posts':posts})

class PostList(ListView):
    model=Post
    ordering='-pk'
    # template_name='blog/index.html'


#FBV
# def single_post_page(request, pk):
#     post=Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post':post, })

#CBV
class PostDetail(DetailView):
    model=Post