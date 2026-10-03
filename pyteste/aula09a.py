# MANIPULAÇÃO DE STRINGS

frase = '   Corso em Vídeo Python   '

print('\n')
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('''\nLorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde 1966, quando os designers da Letraset e James Mosley, o bibliotecário da St Bride Printing Library em Londres, pegaram uma tradução de Cícero de 1914 e a embaralharam para criar um texto fictício para as folhas de tipos da Letraset. Ele sobreviveu não apenas a muitas décadas, mas também à transição para a editoração eletrônica, permanecendo essencialmente inalterado. Foi popularizado graças a essas folhas e, mais recentemente, com softwares de editoração eletrônica como o Aldus PageMaker e o Microsoft Word, que incluíam versões de Lorem Ipsum\n''')
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #  não salvou, apenas exibe a troca neste ponto. Se quser salvar, coloque em uma nova variável chamada frase.
print('Curso' in frase) # retorna True ou False
print(frase.find('Curso')) # retorna o índice em que a palavra começa.
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
