import json
import os

dadoslivros = dict()
livros = list()



def linha (tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg): #tratamento de erro
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Erro, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
############################Arquivo Json######################


def guardalivro(livros):
    with open('projeto.json', 'w') as file:
        json.dump(livros, file)

def ler_json():
    livros = {}
    if os.path.exists('projeto.json'):
        with open('projeto.json', 'r') as file:
            livros = json.load(file)


    return livros

############################/\/\/\######################

def menu (lista): #imprime o menu
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def deletarlivro(): #deleta o livro que o usuario informar
        select = int(input('Informe o COD do livro que deseja deletar: '))
        del livros[select]
        print(livros)


def encontrar(elemento): #faz a pequisa
    lista_pos = []  # apenas pra informar os livros da pesquisa.
    for k, v in enumerate(livros):
        print('toaquui3')
        if elemento in v.values():
            print("to aqui")
            lista_pos.append(livros[k])
    print('-=' * 58)
    print('| cod ', end='')
    for i in dadoslivros.keys():
        print(f'| {i:<14}', end='')
    print()
    print('-=' * 58)
    for k, v in enumerate(lista_pos):
        print(f'| {k:>3}', end='')
        for d in v.values():
            print(f' | {str(d): <13}', end='')
        print()

def dellivrosanos(elemento): #deleta todos os livros com o mesmo ano informado
    for i in range(len(livros)):
        for k, v in enumerate(livros):
            print('toaquui3')
            if elemento in v.values():
                print("to aqui")
                del livros[k]
    print('-=' * 58)
    print('| cod ', end='')
    for i in dadoslivros.keys():
        print(f'| {i:<14}', end='')
    print()
    print('-=' * 58)
    for k, v in enumerate(livros):
        print(f'| {k:>3}', end='')
        for d in v.values():
            print(f' | {str(d): <13}', end='')
        print()



def mostrarlivros(): #mostra os livros
    print('-=' * 58)
    print('| cod ', end='')
    for i in dadoslivros.keys():
        print(f'| {i:<14}', end='')
    print()
    print('-=' * 58)
    for k, v in enumerate(livros):
        print(f'| {k:>3}', end='')
        for d in v.values():
            print(f' | {str(d): <13}', end='')
        print()



def cadastrolivro(): #faz o cadastro de livros 
    while True:
        dadoslivros.clear()
        dadoslivros['Categoria'] = (str(input('Categoria do livro: ')))
        dadoslivros['Tematica'] = (str(input('Tematica do livro: ')))
        dadoslivros['Ano'] = leiaInt('Ano do livro: ')
        dadoslivros['Titulo'] = (str(input('Titulo do livro: ')))
        dadoslivros['Autor'] = (str(input('Autor do livro: ')))
        dadoslivros['Assunto'] = (str(input('Assunto do livro: ')))
        dadoslivros['Quantidade'] = leiaInt('Informe a quantidade de livros desse modelo: ')
        livros.append(dadoslivros.copy())

        while True:
            resp = str(input('Deseja Continuar? [S/N] ')).upper()
            if resp in 'SN':
                break
            print('Erro! Responda apenas S ou N')
        if resp == 'N':
            break
    print('-=' * 30)

livros = ler_json() # Carregar dados na list livros

while True:
    resposta = menu(['Cadastrar Livro', 'Mostrar livros', 'Deletar livro', 'Pesquisar livros', 'Pesquisar por ano', 'Deletar todos os livros no Ano', 'Para sair do programa'])
    if resposta == 1:
        cadastrolivro()
    elif resposta == 2:
        mostrarlivros()
    elif resposta == 3:
        deletarlivro()
    elif resposta == 4:
        opcao= str(input('Informe algo: '))
        print(encontrar(opcao))
    elif resposta == 5:
        opcao = int(input('Informe o ano para pesquisar: '))
        encontrar(opcao)
    elif resposta == 6:
        opcao = int(input('Informe o ano para deletar todos os livros do ano informado: '))
        dellivrosanos(opcao)
    elif resposta == 7:
        guardalivro(livros)
        break
    else:
        print('Erro!  Digite uma opcao válida!')

menu()