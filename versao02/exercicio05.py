nome = input('Digite o nome do aluno: ')

notas = []
quantidade_de_notas = 6

i = 0
while i < quantidade_de_notas:
    nota = float(input('Digite sua nota:'))
    notas.append(nota)
    i += 1 

print('Notas do aluno {}:'.format(nome))
for nota in notas:
    print('Nota: {}'.format(nota))

soma = 0
for nota in notas:
    soma += nota

print('Total de pontos alcançados: {}'.format(soma))

media = soma / quantidade_de_notas

print('Média obtida: {}'.format(media))

if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')