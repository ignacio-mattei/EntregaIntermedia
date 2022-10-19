from asyncio.base_subprocess import ReadSubprocessPipeProto
from django.shortcuts import render, redirect
from .forms import FormNoticia, BusquedaNoticia, FormPublicacionRedes, FormReferencia
from .models import Noticia, PublicacionRedes, Referencia
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')


def crear_noticia(request):    
    if request.method == 'POST':
        form = FormNoticia(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            noticia = Noticia(
                titulo=data.get('titulo'),
                contenido=data.get('contenido'),
                fecha_creacion=fecha
            )
            noticia.save()

            return redirect('listado_noticias')
        
        else:
            return render(request, 'crear_noticia.html', {'form': form})
            
    
    form_noticia = FormNoticia()
    
    return render(request, 'crear_noticia.html', {'form': form_noticia})

def crear_referencia(request):    
    if request.method == 'POST':
        form = FormReferencia(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            referencia = Referencia(
                titulo=data.get('titulo'),
                link=data.get('link'),
                fecha_creacion=fecha
            )
            referencia.save()

            return redirect('listado_noticias')
        
        else:
            return render(request, 'crear_referencia.html', {'form': form})
            
    
    form_referencia= FormReferencia()
    
    return render(request, 'crear_referencia.html', {'form': form_referencia})

def crear_publicacionRedes(request):    
    if request.method == 'POST':
        form = FormPublicacionRedes(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            publicacionRedes = PublicacionRedes(
                titulo=data.get('titulo'),
                redsocial=data.get('redsocial'),
                fecha_creacion=fecha
            )
            publicacionRedes.save()

            return redirect('listado_noticias')
        
        else:
            return render(request, 'crear_publicacionRedes.html', {'form': form})
            
    
    form_publicacionRedes= FormPublicacionRedes()
    
    return render(request, 'crear_publicacionRedes.html', {'form': form_publicacionRedes})

def listado_noticias(request):
    
    listado_noticias = Noticia.objects.all() 
    listado_referencias= Referencia.objects.all() 
    listado_publicacionRedes=PublicacionRedes.objects.all()
    form = BusquedaNoticia()
       
    return render(request, 'listado_noticias.html', {'listado_noticias': listado_noticias,'listado_referencias': listado_referencias,'listado_publicacionRedes': listado_publicacionRedes, 'form' : form})
   

def busqueda_noticias(request):
    
    busqueda_titulo = request.GET.get('titulo')
    print(busqueda_titulo)
    
    if busqueda_titulo:
        busqueda_noticias = Noticia.objects.filter(titulo__icontains=busqueda_titulo)
    else:
        busqueda_noticias = Noticia.objects.all()
    
    form = BusquedaNoticia()
    return render(request, 'busqueda_noticias.html', {'busqueda_noticias': busqueda_noticias, 'form': form})


def nosotros(request):
    return render(request, 'nosotros.html')