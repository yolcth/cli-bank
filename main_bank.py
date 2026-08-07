from uteis import util
from time import sleep
from uteis import cadastro
from uteis import interface
import json

arquivo = 'python/projects/bank/json/historico.json'
util.menu()

while True:
    lista = [
        '1 - Sou cadastrado, quero fazer o Login',
        '2 - Não sou cadastrado, quero me cadastrar',
        '3 - Quero sair do banco'
    ]
    for i in lista:
        print(i)
    try:
        situacao = int(input('\nQual operação você deseja realizar? [1/3]: '))
    except ValueError:
        print('\033[31mErro: Usuário digitou fora dos parametrôs pedidos.\033[m') 
        continue  

    if situacao == 2:
        try:
            interface.texto('Seu Cadastro')
            nome = str(input('Digite o seu nome: '))
            idade = int(input('Digite a sua idade: '))
        except (ValueError, NameError):
            print('\033[31mrro. Tente novamente respondendo da forma correta.\033[m')
            continue
        if idade < 18:
            print('Você é menor de idade. Não pode se cadastrar.')
            break
        senha = str(input('Digite a sua senha: '))
        cadastro.cadastrar(arquivo, nome, idade, senha) # passando todos os parametros

    elif situacao == 3:
        print('Até logo.')
        break

    if situacao == 1:
        interface.texto('Seu Login')
        usuario = str(input('Digite o seu nome: '))
        senha = str(input('Digite a sua senha: '))
        try:
            conta, logado = cadastro.login(arquivo, usuario, senha)
        except TypeError:
            print('\033[31mErro. Usuário não encontrado.\033[m')
            continue
        except FileNotFoundError:
              print('\033[31mErro: o arquivo de histórico não foi encontrado.\033[m')
              continue
        except json.JSONDecodeError:
            print('\033[31mErro: o arquivo de histórico está corrompido ou mal formatado.\033[m')
            continue

        if logado == True:
            while True:
                util.options()
                sleep(0.5)
                try:
                    escolha = int(input('\nO que você deseja fazer? (1/5): '))
                    print()
                except ValueError:
                    print('\033[31mErro: Usuário digitou fora dos parametrôs pedidos.\033[m') 
                    continue

                if escolha == 5:
                    print('Muito obrigado por usar o nosso sistema bancário! Volte sempre!\n')
                    exit()

                elif escolha == 1:
                    util.ver_saldo(conta['saldo'])

                elif escolha == 2:
                    deposito = util.depositar_dinheiro(conta['saldo'])
                    conta['saldo'] += deposito 
                    util.atualizar_conta(arquivo, conta['nome'], conta['saldo'], 'deposito', deposito)

                elif escolha == 3:
                    retirar = util.retirar_dinheiro(conta['saldo'])
                    if retirar > conta['saldo']:
                            print('Erro, Não dá para retirar esse valor.') 
                            continue
                    
                    conta['saldo'] -= retirar # o saldo da conta vai ser o saldo menos o valor retirado
                    util.atualizar_conta(arquivo, conta['nome'], conta['saldo'], 'saque', retirar)

                elif escolha == 4:
                    novo_saldo, valor = util.transferencia(conta['saldo'])
                    if novo_saldo is not None: # se novo saldo não for retornado em None (nada)
                        conta['saldo'] = novo_saldo 
                        util.atualizar_conta(arquivo, conta['nome'], conta['saldo'], 'pix', valor)
                else:
                    print('Número inválido.')

        elif logado == False:
            print('Não encontramos a conta. Nome ou senha inválidos.\n')
            break
