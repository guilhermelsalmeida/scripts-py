cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

nome = input('\nQual é o seu nome? ').capitalize().strip()

print(f'{cores["fundoamareloletrapreta"]} É um prazer te conhecer, {nome}!!! {cores["limpo"]}')
