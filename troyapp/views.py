from distutils.command.install_egg_info import safe_name
from gc import get_objects
from this import d
from tkinter import DISABLED
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    if request.method == "GET":  
      return render(request,'index.html')
  
    elif request.method == "POST":
        
        dicionario = {k: v or 0 for (k, v) in request.POST.items()}
        velocidade_troy = float(dicionario['velocidade_troy'])
        avanco_troy = float(dicionario['avanco_troy'])
        comprimento_troy = float(dicionario['comprimento_troy'])
        preco_pastilha_troy = float(dicionario['preco_pastilha_troy'])
        arestas_troy = float(dicionario['arestas_troy'])
        pastilha_ferramenta_troy = float(dicionario['pastilha_ferramenta_troy'])
        pastilha_alisadora_troy = float(dicionario['pastilha_alisadora_troy'])
        qtde_alisadora_troy = float(dicionario['qtde_alisadora_troy'])
        past_alisa_ferramenta_troy = float(dicionario['past_alisa_ferramenta_troy'])
        vida_util_troy = float(dicionario['vida_util_troy'])
        vida_util_alisa_troy = float(dicionario['vida_util_alisa_troy'])
        prod_anual_troy = float(dicionario['prod_anual_troy'])
        
        velocidade = float(dicionario['velocidade'])
        avanco= float(dicionario['avanco'])
        comprimento= float(dicionario['comprimento'])
        preco_pastilha = float(dicionario['preco_pastilha'])
        arestas = float(dicionario['arestas'])
        pastilha_ferramenta = float(dicionario['pastilha_ferramenta'])
        pastilha_alisadora = float(dicionario['pastilha_alisadora'])
        qtde_alisadora = float(dicionario['qtde_alisadora'])
        past_alisa_ferramenta = float(dicionario['past_alisa_ferramenta'])
        vida_util = float(dicionario['vida_util'])
        vida_util_alisa = float(dicionario['vida_util_alisa'])
        prod_anual = float(dicionario['prod_anual'])
        
        
        try:
          tempo_usinagem_troy = comprimento_troy / avanco_troy
          tempo_usinagem = comprimento / avanco
    
          ganho_produtividade = 1 - (tempo_usinagem_troy/tempo_usinagem)
          custo_anual_troy = 0
          custo_anual = 0
          
          if preco_pastilha_troy == 0:
            custo_anual_troy = 0
          elif pastilha_alisadora_troy == 0:
            custo_anual_troy = (preco_pastilha_troy * pastilha_ferramenta_troy) / (arestas_troy * vida_util_troy)
          elif pastilha_alisadora_troy >= 1:
            custo_anual_troy = ((preco_pastilha_troy * pastilha_ferramenta_troy) / (arestas_troy * vida_util_troy)) + ((pastilha_alisadora_troy / past_alisa_ferramenta_troy) / (qtde_alisadora_troy / vida_util_alisa_troy ))
          else: 
            custo_anual_troy = 0
            
          if preco_pastilha == 0:
            custo_anual = 0
          elif pastilha_alisadora_troy == 0:
            custo_anual = (preco_pastilha * pastilha_ferramenta) / (arestas * vida_util)
          elif pastilha_alisadora_troy >= 1:
            custo_anual = ((preco_pastilha * pastilha_ferramenta) / (arestas * vida_util)) + ((pastilha_alisadora / past_alisa_ferramenta) / (qtde_alisadora / vida_util_alisa ))
          else: 
            custo_anual = 0
            
          custo_ferramenta_ano_troy = custo_anual_troy * prod_anual_troy
          custo_ferramneta_ano = custo_anual * prod_anual
            
          
          
          dados = {'troy' :  custo_ferramenta_ano_troy,
                   'conco' : custo_ferramneta_ano,
                   'prod': ganho_produtividade }
          
        
          
          
          print(velocidade_troy)
          print(avanco_troy)
          print(comprimento_troy)
          print(preco_pastilha_troy)
          print(arestas_troy)
          print(pastilha_ferramenta_troy)
          print(pastilha_alisadora_troy)
          print(qtde_alisadora_troy)
          print( past_alisa_ferramenta_troy)
          print(vida_util_troy)
          print(vida_util_alisa_troy)
          print(prod_anual_troy)
          print(velocidade)
          print(avanco)
          print(comprimento)
          print(preco_pastilha)
          print(arestas)
          print(pastilha_ferramenta)
          print(pastilha_alisadora)
          print(qtde_alisadora)
          print( past_alisa_ferramenta)
          print(vida_util)
          print(vida_util_alisa)
          print(prod_anual)
          print('Tempo de usinagem troy: ', round(tempo_usinagem_troy, 2))
          print('Tempo de usinagem: ', round(tempo_usinagem, 2))
          print('Custo anual troy: ', round(custo_anual_troy, 2))
          print('Custo anual: ', round(custo_anual_troy, 2))
          print('Custo Ferramenta / ano troy: ', custo_ferramenta_ano_troy)
          print('Custo Ferramenta / ano : ', custo_ferramneta_ano)
          
          return render(request,'analise.html',dados)
          
        except ZeroDivisionError:
          print('Erro')
          
          
        
        
      

    



