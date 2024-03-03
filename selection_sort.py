def buscaMenorIndice(arr):
    menor = arr[0]   # valor do menor elemento
    menor_elemento_indice = 0 # índice do menor elemento
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_elemento_indice = i
    return menor_elemento_indice # retorna o índice do menor elemento dessa lista

def ordenacaoporSelecao(arr):
    novoArr = []    
    for i in range(len(arr)):
        menor = buscaMenorIndice(arr)
        novoArr.append(arr.pop(menor))

    return novoArr

arr = [5, 3, 4, 5, 8, 10, 25, 563, 43, 23, 235, 34532]

print(f'Array original antes do algoritimo: {arr}')
print(f'Array ordenado: {ordenacaoporSelecao(arr)}')
print(f'Array original depois do algoritimo: {arr}')