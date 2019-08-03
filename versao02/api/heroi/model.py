herois = [
    {"id": 1, "nome": "Hulk"},
    {"id": 2, "nome": "Thor"},
    {"id": 3, "nome": "Homem-aranha"}
]

def incluir_heroi(nome):
    id = len(herois) + 1
    heroi = {"id": id, "nome": nome}

    herois.append(heroi)