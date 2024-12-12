from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def note_list(request):
    tasks = Post.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/list.html', ctx)

def note_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        if title and content and date:
            Post.objects.create(
                title = title,
                content = content,
                date = date,
            )
            return redirect('tasks:list')
    return render(request, 'tasks/form.html')

def note_detail(request, pk):
    tasks = get_object_or_404(Post, pk=pk)
    ctx = {'tasks': tasks}
    return render(request, 'tasks/detail.html', ctx)

def note_update(request, pk):
    tasks = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        if title and content and date:
            tasks.title = title
            tasks.content = content
            tasks.save()
            return redirect(tasks.get_detail_url())
    ctx = {'tasks': tasks}
    return render(request, 'tasks/form.html', ctx)

def note_delete(request, pk):
    tasks = get_object_or_404(Post, pk=pk)
    tasks.delete()
    return redirect('tasks:list')






