#ALGORITMO PARA LISTA DE COMPRAS
#aqui é importado as funções que vão ser utilizadas.
#obs: caso queira entender o motivo delas serem usadas nas condições especificas, vá nos comentários das funções
from função_1 import func_1
from função_2 import func_2
from função_3 import func_3
from função_4 import func_4
from função_5 import func_5
from função_6 import func_6
menu=open('menu.txt', 'r') #aqui é aberto o arquivo que contém o menu de instruções
print(menu.read()) #aqui é impresso o menu de instruções na tela
menu.close() #aqui fechamos o arquivo
variavel_controle_repetição='s' #variável que determina a condição para qual repetimos os programa
while (variavel_controle_repetição=='s'): #repetição
    variavel_controle_condição=input('digite a opção desejada: ') #variável que determina qual a ação que vai ser executada pelo usuario
    if variavel_controle_condição=='c': #condição  de criação da lista e adição dessa lista nos arquivos
#leia  os comentários das funções aqui usadas        
        matriz=func_1('lista_de_compras.txt')
        elemento_matriz=func_2(matriz)
        func_6(elemento_matriz)
    elif variavel_controle_condição=='v': #condição para ver a lista impressa na tela
#leia  os comentários das funções aqui usadas 
        elemento_matriz=func_1('lista_de_compras.txt')
        func_5(elemento_matriz)
    elif variavel_controle_condição=='r': #condição que remove linha da lista de compras
#leia  os comentários das funções aqui usadas 
        elemento_matriz=func_1('lista_de_compras.txt')
        elemento_matriz_2=func_3(elemento_matriz)
        func_6(elemento_matriz_2)
    elif variavel_controle_condição=='e': #condição de edição da linha específica dada pelo usuario
#leia  os comentários das funções aqui usadas 
        elemento_matriz=func_1('lista_de_compras.txt')
        elemento_matriz_2=func_4(elemento_matriz)
        func_6(elemento_matriz_2)
    else: #condição que abarca o caso do usuario ter digitado errado
        print('Infelizmente você pressionou errado')
    variavel_controle_repetição=input('caso queira fazer outra coisa ou refazer digite s, caso não digite n: ')
mensagem_despedida=open('mensagem_despedida.txt', 'r') #aqui é aberto o arquivo que contém uma mensagem de despedida
print(mensagem_despedida.read()) #aqui a mensagem é impressa na tela
mensagem_despedida.close() #aqui o arquivo é fechado e algoritmo finaliza sua execução