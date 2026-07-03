
from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Author



def home(request):
    query = request.GET.get('q')

    if query:
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.all()

    return render(request, 'blog/home.html', {'blogs': blogs})


def add_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        author_id = request.POST.get('author')
        author = get_object_or_404(Author, id=author_id)

        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)

        content = request.POST.get('content')

        Blog.objects.create(
            title=title,
            author=author,
            category=category,
            content=content,
            image=image
)
        

        return redirect('/')

    categories = Category.objects.all()
    authors = Author.objects.all()

    return render(request, 'blog/add.html', {
        'categories': categories,
        'authors': authors
    })


def detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    # Increase views
    blog.views += 1
    blog.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()

            return redirect('detail', id=blog.id)

    else:
        form = CommentForm()

    comments = blog.comment_set.all().order_by('-created_at')

    return render(request, 'blog/detail.html', {
        'blog': blog,
        'form': form,
        'comments': comments
    })


def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        blog.title = request.POST.get('title')

        author_id = request.POST.get('author')
        blog.author = get_object_or_404(Author, id=author_id)

        category_id = request.POST.get('category')
        blog.category = get_object_or_404(Category, id=category_id)
        blog.content = request.POST.get('content')

        image = request.FILES.get('image')

        if image:
         blog.image = image

        blog.save()

        return redirect('/')

    categories = Category.objects.all()
    authors = Author.objects.all()

    return render(request, 'blog/update.html', {
        'blog': blog,
        'categories': categories,
        'authors': authors
    })


def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('/')


def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('/categories/')

    return render(request, 'blog/category.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


def blogs_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    blogs = Blog.objects.filter(category=category)

    return render(request, 'blog/category_blogs.html', {
        'category': category,
        'blogs': blogs
    })


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('/categories/')


def add_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        Author.objects.create(
            name=name,
            email=email,
            bio=bio
        )

        return redirect('/')

    return render(request, 'blog/author.html')


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    blog.likes += 1
    blog.liked = True

    blog.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))
def liked_blogs(request):
    blogs = Blog.objects.filter(liked=True)
    return render(request, 'blog/liked.html', {'blogs': blogs})


def unlike_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.liked = False
    blog.save()
    return redirect('/liked/')