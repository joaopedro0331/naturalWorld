from django.urls import path, include
from empresa import views

urlpatterns = [    
    path('', views.empresa, name='empresa'),
    path('empresas_contratadas', views.empresas_contratadas, name='empresas_contratadas'),
    path('contratos', views.contratos, name='contratos'),
    path('contratar_empresa/<int:empresa_id>/', views.contratar_empresa, name='contratar_empresa'),
    path('descontratar_empresa/<int:empresa_id>', views.descontratar_empresa, name='descontratar_empresa'),
    path('descontratar_usuario/<int:user_id>/', views.descontratar_usuario, name='descontratar_usuario'),
    path('email_empresa', views.email_empresa, name='email_empresa'),
]