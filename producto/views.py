from django.shortcuts import render, get_object_or_404, redirect, render
from .models import Producto
from .form import ProductoForm

## Vista de incio ##
def home(request):
    return render(request, 'productos/home.html')

## Listas productos ##
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})


## Crear productos ##
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()

    return render(request, 'productos/producto_form.html', {
        'form': form,
        'modo': 'Crear'
    })


## Editar productos ##
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/producto_form.html', {
        'form': form,
        'modo': 'Editar'
    })


## Eliminar productos ## 
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')

    return render(request, 'productos/confirm_delete.html', {
        'producto': producto
    })
