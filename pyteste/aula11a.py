# SISTEMA DE CORES NO TERMINAL

cores = {'limpa': '\033[m', # lista de cores através de dicionário
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7;30m'}

print('\n\033[4;37;42mOlá, Mundo!\033[m') # sublinhado, texto branco e fundo verde
print('\033[0;30;43mOlá, Mundo!\033[m') # normal, texto preto e fundo amarelo
print('\033[7;37mOlá, Mundo!\033[m\n') # fundo branco e letra preta

num1 = 3
num2 = 5

print(f'Os valores são: {cores["verde"]}{num1}{cores["limpa"]} e \033[1;37;41m {num2} \033[m')
print(f'Os valores são: \033[1;37;42m {num1} \033[m e \033[0;31m{num2}\033[m\n')
