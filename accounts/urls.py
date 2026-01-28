from django.urls import path
from . import views

urlpatterns = [
    
    ## Ruta para login ##
    path('login/', views.login_view, name='login'),

    ## Ruta para logout ##
    path('logout/', views.logout_view, name='logout'),

    ## Ruta para el dashboard (protegida) ##
    path('dashboard/', views.dashboard_view, name='dashboard'),

]