from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('pasei')
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario resgistrado com sucesso')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )


def login_views(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')

        messages.error(request, 'Login invalido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


def logout_views(request):
    auth.logout(request)
    return redirect('contact:login')