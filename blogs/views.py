from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """Выводит список тем."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def add_blog(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = BlogForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/add_blog.html', context)


def edit_blog(request, blog_id):
    """Редактирует существующую запись."""
    blog = BlogPost.objects.get(id=blog_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = BlogForm(instance=blog)
    else:
        # Отправка данных POST; обработать данные.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/edit_blog.html', context)


