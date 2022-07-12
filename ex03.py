#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 12/07/2022
#
# 3. #função recursiva
# escreva uma função que receba uma string e retorne outra string de forma reversa.
# # 01-recursiva-reverso
def reverso(valor): # função recursiva
    if len(valor) == 1: # condição de parada
        return valor # retorna o valor da string
    else:
        return reverso(valor[1:]) + valor[0] # chama a função recursiva e faz o cálculo da string reversa

# programa principal
valor = input("Digite uma string: ") # lê a string e armazena na variável valor
print(f"O reverso da string é: {reverso(valor)}") # faz a impressão do reverso da string
