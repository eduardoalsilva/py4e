# Exercício 1: Escreva uma função chamada corte que recebe uma lista e
# a modifica, removendo o primeiro e o último elemento, e retorna None.
# Depois escreva uma função chamada meio que recebe uma lista e retorna
# uma nova lista que contém todos, menos o primeiro e o último elemento.

def cuting(arr):
    arr2 = arr[1:-1]
    print(arr2)

def mid_elements(arr):
    mid = arr[1:-1]
    return mid

elements = input().split()
print(mid_elements(elements))
cuting(elements)
