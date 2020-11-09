from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar las carreras de la bd
    path('listarTrago', views.listar_trago, name="listar_trago"),

    # agregar una carrera    
    path('agregarTrago', views.agregar_trago, name="agregar_trago"),

    # editar una carrera
    path('editarTrago/<int:trago_id>', login_required(views.editar_trago) ,name="editar_trago"),

    # borrar una carrera
    path('borrarTrago/<int:trago_id>', login_required(views.borrar_trago), name="borrar_trago"),

    path('agregaTrago', views.TragoCreate.as_view(), name="agrega_trago"),

    path('listTrago/', views.TragoList.as_view(), name='list_trago'),


    path('editTrago/<int:pk>', views.TragoUpdate.as_view(), name='edit_trago'),

    path('delTrago/<int:pk>', views.TragoDelete.as_view(), name='del_trago'),
]

