from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    
    path('api_articulos/', views.api_articulos, name='api_articulos'),
    path('api_articulos_detalle/<int:pk>/', views.api_articulos_detalle, name='api_articulos_detalle'),

]
