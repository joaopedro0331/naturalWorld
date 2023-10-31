from django.urls import path
from accounts import views

urlpatterns = [
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_usuario_empresa', views.cadastrar_usuario_empresa, name='cadastrar_usuario_empresa'),
    path('profile', views.profile, name='profile'),
    path('editprofile/<int:user_id>/', views.editprofile, name='editprofile'),
]