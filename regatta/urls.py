from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('regattas/', views.regattas, name='regattas'),
    path('regattas/<int:pk>/', views.regatta, name='regatta'),
    path('boats/', views.boats, name='boats')
]