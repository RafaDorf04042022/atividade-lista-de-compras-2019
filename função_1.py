#FUNÇÃO "1"
#essa função ler o arquivo e retorna uma matriz
def func_1(path):
    arq = open(path, 'r') #abre o arquivo em modo leitura
    list_1 = arq.readlines() #cria uma lista que recebe as linhas do arquivo como elemento
    arq.close()
    matriz = [] #variavel que recebe a matriz
    line_matriz = [] #variavel que recebe os valores de cada linha
    for line in range(len(list_1)): #executa uma variavel controle por um periodo igual o numero de elementos da matriz
        line_matriz.append((list_1[line].replace('\n', ''))) #adiciona valores da lista inicial nas linhas da matriz 
        if len(line_matriz) == 3: #determina o tamanho das linhas para adicionar na matriz
            matriz.append(line_matriz) #adiciona na matriz
            line_matriz = [] #limpa a variavel que recebe a linha para pular para outra
    return matriz