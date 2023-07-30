from django.shortcuts import render, redirect
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants


def home(request):
    contas = Conta.objects.all()
    total = 0
    for i in contas:
        total += i.valor
    return render(request, 'home.html', {'contas': contas, 'total': total})


def gerenciar(request):
    contas = Conta.objects.all()
    categoria = Categoria.objects.all()
    total_contas = 0
    for conta in contas:
        total_contas += conta.valor
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas, 'categoria': categoria})


def cadastrar_banco(request):
    apelido = str(request.POST.get('apelido')).capitalize().strip()
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = str(request.POST.get('valor')).strip()
    icone = request.FILES.get('icone')


    #Validacao para ser salvo no db
    if len(apelido) == 0 or len(valor) == 0:
         #mensagen de erro caso nao seja validado o formulario
        messages.add_message(request, constants.ERROR, 'Prenecha todos os campos!')
        return redirect('/perfil/gerenciar')

    conta = Conta(apelido=apelido, banco=banco, tipo=tipo, valor=valor, icone=icone)

    conta.save()
    #mensagem de sucesso
    messages.add_message(request, constants.SUCCESS, 'Novo banco adcionado com sucesso!')
    return redirect('/perfil/gerenciar')


def deletar_banco(request, id):
    banco = Conta.objects.get(id=id)
    print(banco)
    banco.delete()
    messages.add_message(request, constants.SUCCESS, f'Banco {banco} deletado com sucesso!')
    return redirect('/perfil/gerenciar')


def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')


def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if categoria.essencial:
        categoria.essencial = False
        categoria.save()
    else:
        categoria.essencial = True
        categoria.save()

    return redirect('/perfil/gerenciar/')