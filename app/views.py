from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    receitas = {
        1:'Lazanha',
        2:'Sopa de Legumes',
        3:'Sorvete',
        4:'Salada de Frutas'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
    

