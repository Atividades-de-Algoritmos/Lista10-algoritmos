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
def ler_temperaturaC(): 
    temperaturaC = float(input("Digite a temperatura em graus Celsius: "))
    return temperaturaC

# b
def calcular_temperaturaF(temperaturaC):
    temperaturaF = (9 * temperaturaC + 160) / 5
    return temperaturaF

# c
def mostrar_temperaturaF(temperaturaF):
    print(f"A temperatura em graus Fahrenheit é:  {temperaturaF}")

# programa principal
temperaturaC = ler_temperaturaC()
temperaturaF = calcular_temperaturaF(temperaturaC)
mostrar_temperaturaF(temperaturaF)
