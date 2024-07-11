import os

from numpy import append

def nome_app():
    print('Restaurante')
def opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Encerrar')
def fim():
    exibir_sub_titulo('Finalizando aplicação')
def voltar_ao_menu_principal():
    input('Escolha a opção certa: ')
    main()
def opcao_invalida():
    print('Opção inválida \n')
    voltar_ao_menu_principal()
def exibir_sub_titulo(texto):
    os.system('clear')
    print(texto)
    print()
def escolha():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Você ativou o restaurante')
        elif opcao_escolhida == 4:
            print('Você encerrou o restaurante')
        elif opcao_escolhida == 5:
            fim()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
restaurantes = [{'nome':'Jalapão', 'categoria':'frutas', 'ativo':True},{'nome':'Furnão', 'categoria':'churrascaria', 'ativo':False}, {'nome':'Sanduba', 'categoria':'sanduiches', 'ativo':False}]
def cadastrar_restaurante():
    adicionar = input('Digite o restaurante que deseja: \n')
    restaurantes.append(adicionar)
    print(f'o restaurante {restaurantes[-1]} foi aidicionado a lista\n')
    exibir_sub_titulo('Cadastrar novo restaurante?')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_sub_titulo('Listando restaurantes:')
    for restaurante in restaurantes:
        print(f'\n * {restaurante}')
    voltar_ao_menu_principal()

def main():
    os.system('clear')
    nome_app()
    opcoes()
    escolha()
    
if __name__ == '__main__':
    main()

