import os
import math
import random

def raiz_quadrada():
    numero = float(input("Digite um numero para calcular a raiz quadrada: "))
    if numero < 0:
        print("Não é possivel calcular a raiz quadrada de numero negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Pressione qualquer tecla para continuar...")

def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
    input("Pressione qualquer tecla para continuar...")

def numero_aleatorio():
    inicio = float(input("Digite o valor inicial do intervalo: "))
    fim = float(input("Digite o valor final do intervalo: "))
    if inicio > fim:
        print(f"O valor inicial deve ser menor ou igual ao valor final!")
    else:
        numero = random.randit(inicio, fim)
        print(f"Numero aleatorio gerado entre {inicio} e {fim}: {numero}")
    input("Pressione qualquer tecla para continuar...")

def calculadora():
    while True:
        os.system("cls")
        print("\n=== Operações ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Divisão")
        print("4 - Multiplicação")
        print("5 - Potencia")
        print("6 - Voltar")
        cal = input("Escolha uma opção: ")
        if cal == '1':
            soma()
        elif cal == '2':
            sub()
        elif cal == '3':
            div()
        elif cal == '4':
            mult()
        elif cal == '5':
            poten()
        elif cal == '6':
            main()
            break
        else:
            print("Opção invalida! Tente novamente")

    def soma(a, b):
        a = float(input("Digite o valor do primeiro numero: "))
        b = float(input("Digite o valor do segundo numero: "))
        return a + b
    input("Pressione qualquer tecla para continuar...")

    def sub(a, b):
        a = float(input("Digite o valor do primeiro numero: "))
        b = float(input("Digite o valor do segundo numero: "))
        return a - b
    input("Pressione qualquer tecla para continuar...")

    def div(a, b):
        a = float(input("Digite o valor do primeiro numero: "))
        b = float(input("Digite o valor do segundo numero: "))
        return a / b
    input("Pressione qualquer tecla para continuar...")

    def mult(a, b):
        a = float(input("Digite o valor do primeiro numero: "))
        b = float(input("Digite o valor do segundo numero: "))
        return a * b
    input("Pressione qualquer tecla para continuar...")

    def poten(a, b):
        a = float(input("Digite o valor do primeiro numero: "))
        b = float(input("Digite o valor do segundo numero: "))
        return a ** b
    input("Pressione qualquer tecla para continuar...")

def main():
    while True:
        os.system("cls")
        print("\n=== MENU DE OPERAÇÕES ===")
        print("1 - Raiz Quadrada")
        print("2 - Potencia")
        print("3 - Numero Randomico")
        print("4 - Calculadora")
        print("5 - Sair")
    
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            raiz_quadrada()
        elif opcao == '2':
            potencia()
        elif opcao == '3':
            numero_aleatorio()
        elif opcao == '4':
            calculadora()
        elif opcao == '5':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção invalida! Tente novamente")

if __name__ == "__main__":
    main()