import os

restaurantes = [{'nome': 'Subenshi', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'Porta35', 'categoria': 'Hamburguer', 'ativo': False}] 

def exibe_nome_programa():
    print("""
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
        """)

def adicionar_restaurante(nome, categoria):
    restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo': False})

def exibe_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurantes')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    exibir_texto('Cadastro de Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:')
    adicionar_restaurante(nome_restaurante, categoria_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado')
    else:
        exibir_texto('Lista de Restaurantes')
        print('Nome'.ljust(20) + ' | ' + 'Categoria'.ljust(20) + ' | Status')
        for restaurante in restaurantes:
            print(f'{restaurante["nome"].ljust(20)} | {restaurante["categoria"].ljust(20)} | ' + (' Ativo' if restaurante['ativo'] else ' Inativo') )
    voltar_menu()

def alternar_estado_restaurante():
    exibir_texto('Ativar/Desativar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'Restaurante {nome_restaurante} está ativo' if restaurante['ativo'] else f'Restaurante {nome_restaurante} está inativo')
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError: # caso o usuário digite um valor inválido
        opcao_invalida()

def opcao_invalida():
    print('Opção inválida')
    voltar_menu()

def finalizar_app():
    os.system('cls')
    exibir_texto('Obrigado por utilizar o sistema de restaurantes!')
    exit()

def voltar_menu():
    input('Pressione qualquer tecla para voltar ao menu...')
    main()

def limpar_tela(): 
    os.system('cls')

def exibir_texto(texto):
    os.system('cls') 
    linha = '*' * (len(texto) + 4) 
    print(linha)
    print(f'* {texto} *')
    print(linha)

def main():
    os.system('cls') # limpa a tela
    exibe_nome_programa()
    exibe_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
