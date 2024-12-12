from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def note_list(request):
    notes = Post.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/list.html', ctx)

def note_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(
                title = title,
                content = content,
            )
            return redirect('notes:list')
    return render(request, 'notes/form.html')

def note_detail(request, pk):
    notes = get_object_or_404(Post, pk=pk)
    ctx = {'notes': notes}
    return render(request, 'notes/detail.html', ctx)

def note_update(request, pk):
    notes = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            notes.title = title
            notes.content = content
            notes.save()
            return redirect(notes.get_detail_url())
    ctx = {'notes': notes}
    return render(request, 'notes/form.html', ctx)

def note_delete(request, pk):
    notes = get_object_or_404(Post, pk=pk)
    notes.delete()
    return redirect('notes:list')






