from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm

def lista_noticias(request):
    noticias = Noticia.objects.all()  # Recuperamos todas las noticias
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})

def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')  # Redirige a la página de lista de noticias
    else:
        form = NoticiaForm()
    return render(request, 'noticias/agregar_noticia.html', {'form': form})
