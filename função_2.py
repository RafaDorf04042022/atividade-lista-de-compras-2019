#FUNÇÃO "2"
#essa função pede os produtos e informações sobre eles para o usuario
def func_2 (matriz):
    variavel_controle = "s" #cria uma variavel que servirão de alcance(range)
    while (variavel_controle == "s"): #condição de repetição
        elementos = [] #linhas que serão elementos para a matriz
#elementos que pertencem a linha são adicionados         
        elementos.append(input("escreva o nome do produto: ")) 
        elementos.append(input("escreva a quantidade de produtos: "))
        elementos.append(input("escreva o valor de cada item: "))
#determina coondição de repetição para ver se continua ou não adicionando produtos e suas informações
        variavel_controle = input("você quer continuar acrescentando novos valores: s para sim e n para não: ")
        matriz.append(elementos) #adiciona as linhas na matriz
    return matriz