from django.urls import path, include
from dicas import views

urlpatterns = [    
    path('', views.dicas, name='dicas'),
    path('dicasedit/<int:dica_id>/', views.dicasedit, name='dicasedit'),
    path('dicadelete/<int:dica_id>/', views.dicadelete, name='dicadelete'),
]
