# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (frase que pode ser lida de frente para trás e de trás para frente da mesma forma, desconsiderando os espaços e acentos). Exemplos: "Após a sopa", "A sacada da casa", "A torre da derrota".

frase = str(input('\nDigite uma frase (não inclua acentos): ')).strip().upper()
palavras = frase.split() # vira uma lista de palavras
tudo_junto = ''.join(palavras)
inverso = ''
# inverso = tudo_junto[::-1] # solução sem FOR (macete do fatiamento)

for letra in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[letra]
print(f'{tudo_junto} | {inverso}')

if inverso == tudo_junto:
    print('Essa frase é um palíndromo!\n')
else:
    print('Essa frase não é um palíndromo.\n')
