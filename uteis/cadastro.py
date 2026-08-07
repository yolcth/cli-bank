import json; from uteis import interface


def cadastrar(arquivo, nome, idade, senha):
        interface.texto('Seu Cadastro')
        saldo = 0 
        transacao = [
        ]
        with open(arquivo, 'r') as a:
            dados = json.load(a)

        novo_cliente = {'nome': nome, 'idade': idade, 'senha': senha, 'saldo': saldo, 'transacao': []}
        dados.append(novo_cliente)

        with open(arquivo, 'w') as a:
            json.dump(dados, a, indent=4)

def login(arquivo, nome, senha):
        with open(arquivo, 'r') as a:
            dados = json.load(a)
            for conta in dados:
                if conta['nome'] == nome and conta['senha'] == senha:
                    print('você esta cadastrado!')
                    interface.texto('Logado Na Conta Com Sucesso.')
                    print(f'Seja bem vindo(a) ao nosso sistema de banco, fizemos o melhor para que o usuário possa ter uma ótima experiência!\n')
                    login = True
                    return conta, login
            return False
        