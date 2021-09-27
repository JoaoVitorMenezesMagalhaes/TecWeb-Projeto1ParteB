from django.shortcuts import render, redirect
from .models import Note, Tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        tag, create = Tag.objects.get_or_create(name=tag)

        if create:
            tag.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title = '{}'.format(title), content = '{}'.format(content), tag = '{}'.format(tag))
        note.save()
        return redirect('index')
   
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def deletar(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id = id)
        note.delete()
        return redirect('index')

def edit(request, id):
    if request.method == "POST":
        note = Note.objects.get(id = id)
        ntitle = request.POST.get("ntitulo")
        ncontent = request.POST.get("ndetalhes")
        note.title = ntitle
        note.content = ncontent
        note.save()
        return redirect('index')
        
