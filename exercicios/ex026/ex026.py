# Faça um programa que leia uma frase qualquer pelo teclado e mostre: 1) Quantas vezes aparece a letra "A"; 2) Em que posição ela aparece pela primeira vez; e 3) Em que posição ela aparece pela última vez.

frase = str(input('\nDigite uma frase: ')).strip().upper()

print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A aparece na posição {frase.find('A')+1}.') # para o Pytho, é posição 0, por isso se deve somar 1.
print(f'A última letra A aparece na posição {frase.rfind('A')+1}.') # procure a partir da direita (right). Também se deve somar 1 para adequar o Python à posição.
