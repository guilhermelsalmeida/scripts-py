cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

n1 = int(input('\nDigite um valor: '))
n2 = input('DIgite outro valor: ')
n2 = int(n2)
s = n1 + n2

print(f'A soma entre {cores["verde"]}{n1}{cores["limpo"]} e {cores["verde"]}{n2}{cores["limpo"]} é igual a {cores["vermelho"]}{s}{cores["limpo"]}\n')
