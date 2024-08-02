from categoria import Categoria
from transacao import Transacao
import os

lista_categoria = []
lista_transacao = []

def cadastrar_categoria():
    nome = input("Digite o Nome da Categoria: ")
    nova_categoria = Categoria(nome=nome)
    print(f"{nome} Foi adicionado a categorias")
    lista_categoria.append(nova_categoria)

    input("[Enter] -> Retornar ao Menu: ")

def cadastrar_transacao():
    descricao = input("Digite a descrição: ")
    valor = float(input("Digite o valor: "))
    
    if lista_categoria:
        for i, c in enumerate(lista_categoria, start=1):
            print(f"[{i}] {c.nome}")

        n = int(input("Selecione categoria: "))

        if 1 <= n <= len(lista_categoria):
            categoria = lista_categoria[n - 1]
    
    else:
        categoria = Categoria(nome="Sem Categoria")

    

    nova_transacao = Transacao(descricao, valor, categoria)

    lista_transacao.append(nova_transacao)

def exibir_categorias():

    for i, c in enumerate(lista_categoria, start=1):
        print(f"[{i}] {c.nome}")


def deletar_categorias():

    exibir_categorias()
    try:
        n = int(input("Selecione: "))

        if 1 <= n <= len(lista_categoria):
            categoria_deletada = lista_categoria[n - 1]
            del categoria_deletada
    except (ValueError, TypeError):
        print("ERROR")

def atualizar_categoria():

    exibir_categorias()
    try:
        n = int(input("Selecione: "))

        if 1 <= n <= len(lista_categoria):
            categoria_atualizar = lista_categoria[n - 1]
            categoria_atualizar.nome
        
    except (ValueError, TypeError):
        print("ERROR")

def exibir_transacao():

    for t in lista_transacao:
        print(f"""
Descrição: {t.descricao}
Valor: R${t.valor:.2f}
Categoria: {t.categoria.nome}""")
    input("\n[Enter] -> Adicionar ao Menu")

def saldo_total():
    total = 0

    for v in lista_transacao:
        total += v.valor

    return total

