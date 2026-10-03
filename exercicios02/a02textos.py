faturamento = 1000

custo = 600

lucro = faturamento - custo

print('O lucro foi de : R$ ', lucro)

# texto = 'O faturamento foi de R$ ' + str(faturamento) + ' e o lucro foi de R$ ' + str(lucro) + '.' Função str(): converte um número em texto ou string

texto = f'O faturamento foi de R$ {faturamento} e o lucro foi de R$ {lucro}.' # f-string: forma mais simples de formatar texto, usando chaves {} para inserir variáveis diretamente no texto

print(texto)


email = ' EMAIL_FALSO@example.com '
email = email.lower() # lower(): todas em minúsculas
email = email.strip() # strip(): ajustar espaços vazios
print(email)

print(len(email)) # len(): contar o número de caracteres, incluindo espaços

posicao = email.find('@') # find(): encontra a posição de um caractere ou palavra, retorna -1 se não encontrar. Retorna a primeira ocorrência no texto.
print(posicao)
print(email[11]) # acessa um caractere específico do texto, usando a posição (indexação começa em 0)
print(email[11:14]) # fatiamento (slicing): extrai uma parte do texto, usando a posição inicial e final (final não é incluída)
# servidor = email[11:] # fatiamento sem posição final: extrai do início até o final do texto

servidor = email[posicao:] # fatiamento usando a posição do caractere '@' para extrair o servidor automaticamente
print(servidor)
print(email[:posicao]) # fatiamento usando a posição do "@" para extrair o nome do usuário automaticamente
print(email[posicao+1:]) # fatiamento usando a posição do "@" para extrair o servidor, sem o "@"


novo_email = email.replace('example.com', 'gmail.com', 2) # replace: substitui uma parte do texto por outra, usando o texto original e o novo texto como argumentos
print(novo_email)


nome = 'guilherme lucas'
nome = nome.capitalize() # capitallize: primeira letra da primeira palavra em maiúscula
print(nome)
nome = nome.title() # title: primeira letra de cada palavra em maiúscula
print(nome)
nome = nome.upper() # tudo em maiúscula
print(nome)


# FORMATAÇÃO NUMÉRICA

faturamento = 1_0_000 # o Python adota o modelo americano. Então, para formatar um número com separação de milhar, usa-se a vírgula, que edita a variável, ou underline, que é apenas para facilitar a visualização do código
custo = 2_620
lucro = faturamento - custo
margem = lucro / faturamento

texto = f'O faturamento foi de R$ {faturamento:,.2f}, o custo foi de R$ {custo:,.2f}, o lucro foi de R$ {lucro:,.2f} e a margem foi de {margem:.2%}.'
# formata o número com separação de milhar. O formato .2f indica que o número deve ser formatado com 2 casas decimais, mesmo que seja um número inteiro. O .2% formata o número como porcentagem, exibindo o número de casas decimais definido
print(texto)


# EXERCÍCIO

nome = 'guilherme lucas silva almeida'
email = 'emailfalsogui@example.com'
posicao = email.find('@')
servidor = email[posicao:]
print(servidor)
primeiro_nome = nome[:9] # também é possível encontrar através da função find()
primeiro_nome = primeiro_nome.capitalize()
mensagem_personalizada = f'O usuário {primeiro_nome} foi cadastrado com sucesso no e-mail: {email}.'
print(mensagem_personalizada)