def buscabinaria(lista, item):
    baixo = 0
    alto = len(lista)

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lis = [1, 2, 3, 4, 5]
valor = buscabinaria(lis, 2)
if valor is None:
    print("seu número não existe no array")
else:
    print(f'seu número está na posição {valor} do array')
