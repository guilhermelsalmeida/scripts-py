# Faça um programa que leia um ano qualquer e mostre se é bissexto.

from datetime import date
ano = int(input('\nDigite um ano qualquer. Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year # pega o ano atual do sistema

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # lembrando que != significa diferente de...
    print(f'O ano de {ano} é bissexto.\n')
else:
    print(f'O ano de {ano} não é bissexto.\n')
