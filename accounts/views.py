from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.models import Group

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        imagem = request.FILES.get('imagem')

        usuario = Usuario(nome=nome, email=email, imagem=imagem)
        usuario.save()
        
        try:
            grupo = Group.objects.get(name='Usuario')
        except Group.DoesNotExist:
            grupo = Group.objects.create(name='Usuario')

        usuario.groups.add(grupo)
        usuario.set_password(senha)
        usuario.save()

    
        login(request, usuario)

        return redirect('home')

    return render(request, 'accounts/cadastrar_usuario.html')

def cadastrar_usuario_empresa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        imagem = request.FILES.get('imagem')
        email = request.POST['email']
        cnpj = request.POST['cnpj']
        descricao = request.POST['descricao']
        senha = request.POST['senha']

        usuario_empresa = Usuario(nome=nome, email=email, cnpj=cnpj, descricao=descricao, imagem=imagem)
        usuario_empresa.save()

        try:
            grupo = Group.objects.get(name='Empresa')
        except Group.DoesNotExist:
            grupo = Group.objects.create(name='Empresa')

        usuario_empresa.groups.add(grupo)
        usuario_empresa.set_password(senha)
        usuario_empresa.save()

        login(request, usuario_empresa)

        return redirect('home')

    return render(request, 'accounts/cadastrar_usuario_empresa.html')

@login_required
def profile(request):
    usuario = request.user

    context = {
        'usuario' : usuario,
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def editprofile(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)
    if request.user.groups.filter(name='Empresa').exists():
        nome = request.POST['nome']
        imagem = request.FILES.get('imagem')
        email = request.POST['email']
        descricao = request.POST['descricao']
        
        user.nome = nome
        user.email = email
        user.imagem = imagem
        user.descricao = descricao
    elif request.user.groups.filter(name='Usuario').exists():
        nome = request.POST['nome']
        email = request.POST['email']
        imagem = request.FILES.get('imagem')
        user.nome = nome
        user.email = email
        user.imagem = imagem

    user.save()
    messages.success(request, 'Perfil Alterado')

    return redirect('profile')

def handler404(request, exception):
    return render(request, 'error/404.html')