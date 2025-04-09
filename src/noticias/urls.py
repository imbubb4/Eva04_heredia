from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),  # Página de inicio que lista todas las noticias
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),  # Detalles de una noticia específica
    path('agregar/', views.agregar_noticia, name='agregar_noticia'),  # Ruta para agregar noticias
]
