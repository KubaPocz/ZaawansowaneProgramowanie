def ZlaczListy(lista1: list, lista2: list) -> list:
    lista =lista1
    for element in lista2:
        if element not in lista:
            lista.append(element)
    return lista

print(ZlaczListy([1, 2, 3], [3,4, 5, 6]))