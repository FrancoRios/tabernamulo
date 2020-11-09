from django.shortcuts import render, redirect
from .models import Trago
from .forms import TragoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def listar_trago(request):
    trago = Trago.objects.all()
    return render(request, "Registro/listar_trago.html", {'trago': trago})


def agregar_trago(request):
    if request.method == "POST":
        form = TragoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_trago")
    else:
        form = TragoForm()
        return render(request, "Registro/agregar_trago.html", {'form': form})

def borrar_trago(request, trago_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Trago.objects.get(id=trago_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_trago')

def editar_trago(request, trago_id):
    # Recuperamos la instancia de la carrera
    instancia = Trago.objects.get(id=trago_id)

    # Creamos el formulario con los datos de la instancia
    form = TragoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TragoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_trago.html", {'form': form})


# --Otra forma usando clases Generics -------
class TragoCreate(CreateView):
    model = Trago
    form_class = TragoForm
    template_name = 'Registro/trago_form.html'
    success_url = reverse_lazy("listar_trago")

class TragoList(ListView):
    model = Trago
    template_name = 'Registro/list_trago.html'
    # paginate_by = 4

class TragoUpdate(UpdateView):
    model = Trago
    form_class = TragoForm
    template_name = 'Registro/trago_form.html'
    success_url = reverse_lazy('list_trago')

        

class TragoDelete(DeleteView):
    model = Trago
    template_name = 'Registro/trago_delete.html'
    success_url = reverse_lazy('list_trago')

    
