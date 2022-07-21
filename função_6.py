#FUNÇÃO "6"
#essa função escreve a matriz no arquivo obs: ela adiciona cada elemento das linhas da matriz em uma linha do arquivo
#sendo assim, vai ser 3 linhas de arquivo para uma linha da matriz
def func_6(matriz):
    arquivo=open('lista_de_compras.txt','w') #arquivo onde vai ser adicionado os valores da lista
    variavel_controle=0 #variavel controle com valor definido em 0 para definir range definitivo menor que determinado valor
    while variavel_controle<len(matriz): #repetição sem mudança de condição no meio, vai repetir até o valor alcançado
#ser referente a quantidade de linhas da matriz      
        variavel_controle_elemento=0 #mesma coisa que na variavel anterior, só os elementos das linhas
        while variavel_controle_elemento<3: #repete essa condição até o range específico de 3
            variavel_elemento=matriz[variavel_controle] #variavel que recebe as linhas
            arquivo.write(str(variavel_elemento[variavel_controle_elemento])) #escreve os elementos das linhas
            arquivo.write('\n')
            variavel_controle_elemento+=1 #passa pra outro elemento
        variavel_controle+=1 #passa pra outra linha
    arquivo.close() #fecha o arquivo