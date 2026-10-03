nome = input('\nDigite seu nome: ').strip().capitalize()

print('Olá, {}! Muito prazer em te conhecer.'.format(nome))

if nome == 'Guilherme':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == nome == 'Pedro' or nome == 'João' or nome == 'Ana' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana Paula Fernanda Beatriz Camila Mariana Ludmila Letícia Luisa Nicole':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('\nTenha um bom dia.\n')
