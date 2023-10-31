from django.shortcuts import render

def permission_required(permission):
    def test_func(user):
        return user.groups.filter(name=permission).exists()

    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'error/403.html', status=403)

        return wrapped_view

    return decorator

EmpresaPermission = permission_required('Empresa')
UsuarioPermission = permission_required('Usuario')