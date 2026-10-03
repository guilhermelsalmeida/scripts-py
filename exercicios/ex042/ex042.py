# Refaça o Desafio 35 dos triângulos (verificar se 3 segmentos de reta podem formar um triângulo), acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero (todos os lados iguais), Isósceles (dois lados iguais) ou Escaleno (todos os lados diferentes).

reta1 = float(input('\nDigite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

print('-' * 55)

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Esses segmentos de reta PODEM formar um triângulo.')
    if reta1 == reta2 == reta3:
        print('Tipo de triângulo: EQUILÁTERO\n')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Tipo de triângulo: ISÓSCELES\n')
    else:
        print('Tipo de triângulo: ESCALENO\n')
else:
    print('Esses segmentos de reta NÃO PODEM formar um triângulo.\n')
