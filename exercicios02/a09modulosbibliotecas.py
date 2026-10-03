# MÓDULOS E BIBLIOTECAS

# Módulos são arquivos que contêm código Python, como funções, classes e variáveis, que podem ser reutilizados em diferentes programas.
# Bibliotecas são coleções de módulos que fornecem funcionalidades adicionais ao Python, permitindo que os desenvolvedores aproveitem código pré-existente para realizar tarefas específicas.

# import os # import: importa uma biblioteca; os: biblioteca que permite interagir com componentes do sistema operacional no qual o código Python está sendo construído.


# print(f'Pasta de trabalho: << {os.getcwd()} >>') # getcwd: exibe a pasta na qual o código está sendo construído.

# lista_arquivos = os.listdir() # listdir: lista os arquivos da pasta em que o código está sendo rodado.
# print(f'Arquivos da pasta acima: {lista_arquivos}')
# print(f'Pasta em que este código está armazenado: {lista_arquivos[2]}')

# lista_arquivos2 = os.listdir('exercicios02')
# print(f'Arquivos da pasta atual: {lista_arquivos2}')
# print(f'Nome do arquivo deste código: {lista_arquivos2[-2]}')

# lista_arquivos3 = os.listdir('exercicios02/arquivosaulpy')
# print(f'Lista de arquivos da pasta Arquivos: {lista_arquivos3}')

# O mais recomendável é aprender as principais funções das principais bibliotecas Python.
# Na construção de praticamente todos os projetos, há alguma biblioteca que facilita o processo.

# for nome_arquivo in lista_arquivos3:
#    if 'txt' in nome_arquivo:
   #     if '22' in nome_arquivo:
  #          os.rename(f'exercicios02/arquivosaulpy/{nome_arquivo}', f'exercicios02/arquivosaulpy/22/{nome_arquivo}')
 #       elif '23' in nome_arquivo:
#            os.rename(f'exercicios02/arquivosaulpy/{nome_arquivo}', f'exercicios02/arquivosaulpy/23/{nome_arquivo}')


# rename: renomeia um arquivo. Está sendo passado do antigo para o novo nome e movido para outra pasta.
# biblioteca requests (requisições): permite integrar o código com API (sistemas) externos.


import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(link)
# get: busca as informações no local indicado.

# print(f'\n{resposta}')
# print(f'\n{resposta.status_code}') # mostra apenas o número (200, 404, 429, etc.)
# print(f'\n{resposta.text}') # mostra o conteúdo da resposta como texto
# print(f'\n{type(resposta)}') # tem que ser diretamente a URL, e não a variável


# CASO A REQUISIÇÃO DÊ CERTO:

if resposta.status_code == 200:
    dic_resposta = resposta.json()
    print(f'\nFormato JSON convertido em dicionário Python: << {dic_resposta} >>')
    for moeda in dic_resposta:
        dic_conversao_moeda = dic_resposta[moeda]
        valor_moeda = dic_conversao_moeda['bid'] # o bid é um parâmetro que dá a conversão da moeda
        valor_moeda = float(valor_moeda)
        nome_moeda = dic_resposta[moeda]['name']
        print(f'\n{nome_moeda } | {moeda}: R$ {valor_moeda:,.2f}')
else:
    print(f'Erro {resposta.status_code}')

# verifica o código de status antes de usar a resposta com a condicional

# {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.1487', 'low': '5.06925', 'varBid': '0.0262', 'pctChange': '0.514658', 'bid': '5.117', 'ask': '5.12', 'timestamp': '1784226897', 'create_date': '2026-07-16 15:34:57'}, 
 #    'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '5.88582', 'low': '5.81058', 'varBid': '0.010243', 'pctChange': '0.175464', 'bid': '5.84795', 'ask': '5.86167', 'timestamp': '1784226837', 'create_date': '2026-07-16 15:33:57'}, 
  #   'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '332386', 'low': '326824', 'varBid': '-2868', 'pctChange': '-0.864', 'bid': '329041', 'ask': '329078', 'timestamp': '1784226901', 'create_date': '2026-07-16 15:35:01'}}