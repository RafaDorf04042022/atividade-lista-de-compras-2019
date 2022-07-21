#FUNÇÃO "4"
#essa função edita uma linha já preenchida com novos elementos
#obs: ela apaga todos os elementos adicionados anteriormente
def func_4(matriz):
    variavel_controle = "s"
    while (variavel_controle == "s"): #mesma noção usada nas funções anteriores, variavel controle que determina condição de repetição
        linha=int(input('qual linha deve ser editada? ')) #determina linha que deve ser editada
        matriz.pop(linha-1) #remove linha que vai ser editada
#processo de adicionar os novos elementos nessa linha
        elementos = []
        elementos.append(input("escreva o nome do produto: "))
        elementos.append(input("escreva a quantidade de produtos: "))
        elementos.append(input("escreva o valor de cada item: "))
#condição de repetição
        variavel_controle = input("você quer continuar acrescentando novos valores: s para sim e n para não: ")
        matriz.insert(linha-1, elementos) #insere a nova linha na localização indicada
    return matriz