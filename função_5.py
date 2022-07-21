#FUNÇÃO 5
#essa função apenas imprime na tela a matriz, sem comentários mais especificos
def func_5(matriz):
    item1_size = item2_size = item3_size = 0
    for linha in matriz:
        #Nesse laço de repetição toda matriz é iterada para pegar informações dos tamanhos de cada categoria de elemento.
        if len(linha[0]) > item1_size:
            #Aqui sera armazenado o tamanho do maior elemento da categoria (nome do produto).
            item1_size = len(linha[0])
        if len(linha[1]) > item2_size:
            # Aqui sera armazenado o tamanho do maior elemento da categoria (quantidade do produto).
            item2_size = len(linha[1])
        if len(linha[2]) > item3_size:
            # Aqui sera armazenado o tamanho do maior elemento da categoria (preço unitário do produto).
            item3_size = len(linha[2])

    #Com esses tamanhos armazenados agora eles serão utilizados para imprimir a matriz de modo que ela fique justificada.
    contador = 1
    print('=' * (item1_size + item2_size + item3_size + 52))
    #Primeiro é preciso novamente iterar sobre a matriz.
    for linha in matriz:
        #Agora é necessário utilizar a função print para imprimir os elementos, nesse caso utilizando uma Fstring
        #Para deixar o texto justificado é necessário utilizar o método .ljust(), que um método de strings
        #Esse método vai garantir que uma string tenha um determinado tamanho, que é passado como parametro
        #Nesse caso esse tamanho vai depender da categoria de elemento da matriz
        #Na Primeira chave abaixo {} o valor que é passado dis respeito a quantidade de algarismo que tem o tamanho da matriz em si.
        #Na segunda, é passado o tamanho do elemento referente a categoria de (nome do produto)
        #Na terceira, é passado o tamanho do elemento referente a categoria de (quantidade do produto)
        #Na ultima, é passado o tamanho do elemento referente a categoria de (preço unitário do produto)
        print(f'| {str(contador).ljust(len(str(len(matriz))))} - Produto: {linha[0].ljust(item1_size)} | Quantidade: {linha[1].ljust(item2_size)} | preço unitário: {linha[2].ljust(item3_size)} |')
        contador += 1
    print('=' * (item1_size + item2_size + item3_size + 52))