from django.urls import path
from . import views

urlpatterns = [
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/actualizar/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]