from time import sleep; import json

def menu():
    print(f'--=--=--' * 4)
    print(f'{'Banco Digital':^32}')
    print(f'--=--=--' * 4)
    print()


def options():
    menu = [
        '1 - Ver Saldo na conta',
        '2 - Depositar dinheiro na conta',
        '3 - Retirar dinheiro da conta',
        '4 - Realizar uma transferência',
        '5 - Ver Histórico de transações',
        '6 - Sair'
    ]
    for i in menu:
        print(i)


def ver_saldo(saldo_inicial):
    print(f'O seu saldo atual é de \033[32m{saldo_inicial}\033[m')
    print('Prossiga: \n')
    

def depositar_dinheiro(saldo_inicial):
    deposito = float(input('Qual é o valor que você deseja depositar para a sua conta? R$'))
    sleep(0.5); print('Depositando..'); sleep(0.5); print('Tudo certo! Novo saldo atualizado.\n')
    return deposito
                    

def retirar_dinheiro(saldo_inicial):
    print(f'Para retirar dinheiro da conta, você tem que estar ciente do seu saldo atual. Sendo ele de: \033[32m{saldo_inicial}R$.\033[m\n')
    retirar = float(input('Quantos R$ você deseja retirar da sua poupança? R$'))
    sleep(0.5); print('Retirando..'); sleep(0.5); print('Tudo certo! Novo saldo atualizado.\n')
    return retirar

def transferencia(saldo_inicial):
    print(f'Para realizar uma transferência, você tem que estar ciente do seu saldo atual. Sendo ele de: {saldo_inicial}R$\n')
    valor = float(input('Primeiro digite a quantia da transferência e se o valor for válido iremos continuar: R$'))

    if valor > saldo_inicial:
        print('Operação inválida, você tentou transferir mais dinheiro do que tem atualmente. Tente novamente. \n')
        return None

    pix = input(f'Tudo certo, agora você precisa digitar o nome completo da pessoa que deseja transferir a quantia de {valor}: ')
    novo_saldo = saldo_inicial - valor
    sleep(0.5)
    print('\nCarregando e fazendo a transferência..'); sleep(0.5)
    print('...'); sleep(0.5)
    print(f'Pronto! transferência realizada para {pix} com sucesso! O seu saldo foi atualizado!. \n')
    return novo_saldo, valor

def atualizar_conta(arquivo, nome, novo_saldo, tipo_transacao, valor):
    with open(arquivo, 'r') as a:
        dados = json.load(a)
    for usuario_dados in dados:
        if usuario_dados['nome'] == nome:
            usuario_dados['saldo'] = novo_saldo
            usuario_dados['transacao'].append({'Tipo': tipo_transacao, 'Valor': valor})
    with open(arquivo, 'w') as a:
        json.dump(dados, a, indent=4)
