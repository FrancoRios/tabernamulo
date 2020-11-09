from django.urls import path, include
from . import views

urlpatterns = [

    # listar las carreras de la bd
    path('listarTrago', views.listar_trago, name="listar_trago"),

    # agregar una carrera    
    path('agregarTrago', views.agregar_trago, name="agregar_trago"),

    # editar una carrera
    path('editarTrago/<int:trago_id>', views.editar_trago ,name="editar_trago"),

    # borrar una carrera
    path('borrarTrago/<int:trago_id>', views.borrar_trago, name="borrar_trago"),

    path('add_trago', views.TragoCreate.as_view(), name="add_trago"),

]
