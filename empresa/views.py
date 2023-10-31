from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Q
from accounts.models import Usuario
from naturalworld.decorators import EmpresaPermission, UsuarioPermission
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core import mail
from django.urls import reverse

@UsuarioPermission
def empresa(request):
    usuario_id = request.user.id
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        print('erro')

    todas_empresas = Usuario.objects.filter(groups__name="Empresa")
    empresas_contratadas = usuario.contrata.all()
    empresas_nao_contratadas = todas_empresas.exclude(Q(id=usuario_id) | Q(contrata=usuario))
    empresas_nao_contratadas = empresas_nao_contratadas.exclude(id__in=empresas_contratadas)

    context = {
        'empresa': empresas_nao_contratadas,
    }

    return render(request, 'empresa/empresa.html', context)

@EmpresaPermission
def contratos(request):
    usuario_id = request.user.id
    
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        print('Usuário não encontrado')

    empresas_contratadas = Usuario.objects.filter(contrata=usuario)

    context = {
        'empresa': empresas_contratadas,
    }

    return render(request, 'empresa/contratos.html', context)

@UsuarioPermission
def contratar_empresa(request, empresa_id):
    if not request.user.is_authenticated:
        return redirect('login')

    usuario = request.user

    empresa = get_object_or_404(Usuario, pk=empresa_id)
    usuario.contrata.add(empresa)

    return redirect('empresa')

@UsuarioPermission
def empresas_contratadas(request):
    if not request.user.is_authenticated:
        return redirect('login')

    usuario = request.user

    empresas_contratadas = usuario.contrata.all()

    context = {
        'empresa': empresas_contratadas,
    }

    return render(request, 'empresa/empresas_contratadas.html', context)

@UsuarioPermission
def descontratar_empresa(request, empresa_id):
    if not request.user.is_authenticated:
        return redirect('login')

    usuario = request.user
    empresa = get_object_or_404(Usuario, pk=empresa_id)
    print(empresa)
    usuario.contrata.remove(empresa)

    messages.success(request, 'Descontratado')

    return redirect('empresas_contratadas')

@EmpresaPermission
def descontratar_usuario(request, user_id):
    empresa = request.user
    usuario = get_object_or_404(Usuario, pk=user_id)
    usuario.contrata.remove(empresa)
    messages.success(request, 'Descontratado')
    return redirect('contratos')

@login_required
def email_empresa(request):
    emailempresa = request.POST['email']
    texto = request.POST['texto']
    user = request.user

    if emailempresa and texto and user:
        try:
            from_email = settings.EMAIL_HOST_USER
            connection = mail.get_connection()
            connection.open()
            email_empresa = mail.EmailMessage(f'Novo contato de {user.nome}', f'{user.nome} com o email: {user.email}\n tem a seguinte dúvida: {texto}', from_email,
            [emailempresa], connection=connection)
            
            email_cliente = mail.EmailMessage(f'Obrigado {user.nome}', f'Olá {user.nome} enviamos seu email para a empresa, esperamos que ele responda o mais rápido possível.', from_email,
            [user.email], connection=connection)
            
            connection.send_messages([email_empresa, email_cliente])
            connection.close()
            messages.add_message(request, messages.SUCCESS, 'Mensagem enviada')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Erro ao enviar a menssagem')
    else:
        messages.add_message(request, messages.ERROR, 'Preencha os campos')
    return redirect(reverse('empresas_contratadas'))