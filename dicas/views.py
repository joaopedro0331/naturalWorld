from django.shortcuts import render, redirect, get_object_or_404
from .models import Dicas
from django.contrib import messages
from naturalworld.decorators import EmpresaPermission, UsuarioPermission
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dicas(request):
    if request.method == 'GET':
        if request.user.groups.filter(name='Empresa').exists():
            dicas = Dicas.objects.filter(empresa=request.user)
        elif request.user.groups.filter(name='Usuario').exists():
            dicas = Dicas.objects.all()
        else:
            dicas = None
        context ={
            'dicas': dicas,
        }
        return render(request, 'dicas/dicas.html', context)

    if request.method == 'POST':
        descricao = request.POST['descricao']
        empresa_id = request.user.id

        nova_dica = Dicas(descricao=descricao, empresa_id=empresa_id)
        nova_dica.save()

        messages.success(request, 'Dica cadastrada')
        
        return redirect('dicas')

@EmpresaPermission
def dicasedit(request, dica_id):
    dica = get_object_or_404(Dicas, id=dica_id)

    if request.method == 'POST':
        descricao = request.POST['descricao']
        dica.descricao = descricao
        dica.save()

        messages.success(request, 'Dica editada')

        return redirect('dicas')
    
@EmpresaPermission
def dicadelete(request, dica_id):
    dica = get_object_or_404(Dicas, id=dica_id)

    dica.delete()

    messages.success(request, 'Dica Excluida')

    return redirect('dicas')