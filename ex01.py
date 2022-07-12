#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 12/07/2022
#
# 1.	 Em linguagem Python, faça um programa que lê uma temperatura em graus Celsius e apresentá-la convertida em
# graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
# e C é a temperatura em graus Celsius.
# OBS: o programa de conter três funções:
# a - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# b - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# c - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

# funções
# a
def ler_temperaturaC():  # função para ler e retorna o valor da temperatura (não recebe parâmetro)
    temperaturaC = float(input("Digite a temperatura em graus Celsius: ")) # lê a temperatura em graus Celsius e armazena na variável temperaturaC
    return temperaturaC # retorna o valor da temperatura em graus Celsius

# b
def calcular_temperaturaF(temperaturaC): # função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
    temperaturaF = (9 * temperaturaC + 160) / 5 # faz o cálculo da temperatura em graus Fahrenheit e armazena na variável temperaturaF
    return temperaturaF # retorna o valor da temperatura em graus Fahrenheit

# c
def mostrar_temperaturaF(temperaturaF): # função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão (recebe como parâmetro a temperatura em graus Fahrenheit)
    print(f"A temperatura em graus Fahrenheit é:  {temperaturaF}") # faz a impressão da temperatura em graus Fahrenheit

# programa principal
temperaturaC = ler_temperaturaC() # chama a função ler_temperaturaC para ler e retorna o valor da temperatura em graus Celsius e armazena na variável temperaturaC
temperaturaF = calcular_temperaturaF(temperaturaC) # chama a função calcular_temperaturaF para fazer o cálculo da temperatura em graus Fahrenheit e armazena na variável temperaturaF
mostrar_temperaturaF(temperaturaF) # chama a função mostrar_temperaturaF para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão da temperatura em graus Fahrenheit
