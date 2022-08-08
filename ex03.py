#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 06/08/2022
#
# 3. Escreva uma função que receba uma string e retorne outra string de forma reversa.

# ! função recursiva !

def reverso(valor): # Criando a função reverso recebendo um valor como parâmetro
    
    if len(valor) == 1: # Se a string for apenas 1 caractere o programa só retorna o valor que veio
        return valor # Retorna o valor da string
    else:
        return valor[::-1] # Usando o fatiamento conseguimos inverter a string, ele vai percorrer toda a string só que ao contrário e vai retornar o valor invertido.

# -- Chamada das funções --

valor = input("Digite uma string: ") # Lê a string e armazena na variável valor

print(f"\nA String original é: {valor}") # Faz a impressão da string original
print(f"O reverso da string é: {reverso(valor)}") # Faz a impressão chamando a função reverso em cima do valor

print('\nFim do programa') # Informando ao usuário que o programa terminou
