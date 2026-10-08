# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('10 primeiros termos da PA:')

# SOLUÇÃO 01
# for i in range(10):
#    termo = primeiro_termo + i * razao
#    print(termo, end=' ')

# SOLUÇÃO 02
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=' ')
print('| ACABOU\n')
