lista = [1,2,3,4,5,6]

for a in lista:
    print(a)

lista_de_nomes = [
    'Jaozinho',
    'Maria',
    'Benedito',
    'Aroldo'
]

for nome in lista_de_nomes:
    print(nome)

print('------------')

i = 0
while i < len(lista_de_nomes):
    print(lista_de_nomes[i])
    i += 1

print('---------------')

lista_de_nomes.append('Faneli')

for nome in lista_de_nomes:
    print(nome)

print('-------------')

del(lista_de_nomes[0])

for nome in lista_de_nomes:
    print(nome)