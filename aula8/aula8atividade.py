nome = 'marcos'
idade = 26
altura = 1.86
peso = 96
imc = peso / (altura ** 2)
ano_atual = 2022
ano_de_nascimento = (ano_atual - idade)
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} é pesa {peso} kg.'.format(nome, idade, altura, peso))
print(f'O IMC de {nome} é {imc:.2f}'.format(nome, imc))
print(f'{nome} nasceu em {ano_de_nascimento}.')