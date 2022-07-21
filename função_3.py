#FUNÇÃO "3"
#essa função remove linha inteira da matriz
def func_3(matriz):
  variavel_controle = "s"
  while (variavel_controle == "s"): #determina condição em que deve ser removida cada linhas
    matriz.pop(int(input("Digite a linha que deve ser removida, sendo que começa em 0: "))) #remove a linha determinada pelo usuario
    variavel_controle = input("você quer continuar removendo valores: s para sim e n para não: ") #determina se deve continuar a condição de repetição
  return matriz