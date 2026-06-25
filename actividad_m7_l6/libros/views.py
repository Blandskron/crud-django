from django.shortcuts import render
from .models import Libro
from .forms import LibroForm

# CRUD - Create, Read, Update, Delete
# Create
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form})

# Read
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

# Update
def actualizar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form})

# Delete
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})