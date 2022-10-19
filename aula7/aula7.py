nome = 'marcos vinicius'
idade = 26
altura = 1.86
e_maior = idade > 18
peso = 96
imc = peso / (altura ** 2)

print (nome, 'tem', idade, 'anos de idade e seu imc é',imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))