from django.urls import path
from . import views


urlpatterns = [
    ## Para listar productos ##
    path('', views.producto_list, name='producto_list'),    

    ## Para crear nuevos productos ##
    path('create/', views.producto_create, name='producto_create'),

    ## Para editar productos ##
    path('<int:pk>/edit/', views.producto_update, name='producto_update'),

    ## Para eliminar productos ##
    path('<int:pk>/delete/', views.producto_delete, name='producto_delete'),
]