
def pesquisa_binaria(lista, item):
    
    baixo = 0
    alto = len(lista) - 1

    print('alto:', alto)

    while baixo <= alto :
        
        meio = (baixo + alto) // 2
        
        chute = lista[meio]
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return 'Elemento nao encontrado na lista'

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 30))


