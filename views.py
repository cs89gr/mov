from django.shortcuts import render_to_response, get_object_or_404,render
from .models import Movies,Category,Director
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def index(request):
    posts = Movies.objects.filter(publisheddate__lte=timezone.now()).order_by('-publisheddate')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response("blog/movies_list.html", {
    'ranking' : Movies.objects.all().order_by('-rating')[:3],
    'likes': Movies.objects.all().order_by('-like')[:3],
    'categories': Category.objects.all(),
    'posts': posts
})


def view_post(request, slug):
    return render_to_response('blog/movies_details.html', {
        'ranking' : Movies.objects.all().order_by('-rating')[:3],
        'likes': Movies.objects.all().order_by('-like')[:3],
        'categories': Category.objects.all(),
        'post': get_object_or_404(Movies,slug=slug)
    })



def view_dir(request, pk):
    post = get_object_or_404(Director, pk=pk)
    return render_to_response('blog/director_details.html', {
        'ranking' : Movies.objects.all().order_by('-rating')[:3],
        'likes': Movies.objects.all().order_by('-like')[:3],
        'categories': Category.objects.all(),
        'post': post
    })



def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Movies.objects.filter(category=category).order_by('-Title')
    return render_to_response('blog/view_category.html', {
        'ranking' : Movies.objects.all().order_by('-rating')[:3],
        'likes': Movies.objects.all().order_by('-like')[:3],
        'categories': Category.objects.all(),
        'posts': posts,
        'category': category
    })

def like_post(request,slug):
 a=get_object_or_404(Movies, slug=slug)
 count=a.like
 count+=1
 a.like=count
 a.save()
 return HttpResponseRedirect ('/view/%s'%slug)
