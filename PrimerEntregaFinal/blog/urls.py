from django.urls import path
from .views import home, crear_noticia, listado_noticias, busqueda_noticias, nosotros, crear_referencia, crear_publicacionRedes

urlpatterns = [
    path('', home, name='home'),
    path('noticias/', listado_noticias, name='listado_noticias'),
    path('crear-referencia/', crear_referencia, name='crear_referencia'),
    path('crear-publicacionRedes/', crear_publicacionRedes, name='crear_publicacionRedes'),
    path('busqueda/', busqueda_noticias, name='busqueda_noticias'),
    path('crear-noticia/', crear_noticia, name='crear_noticia'),
    path('nosotros/', nosotros, name='nosotros')
]