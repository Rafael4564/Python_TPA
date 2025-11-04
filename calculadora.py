# -*- coding: utf-8 -*-
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def menu():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potencia")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '6':
            print("Saindo... Até mais!")
            break

        if opcao not in ['1', '2', '3', '4', '5']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: digite apenas números!")
            continue

        if opcao == '1':
            resultado = soma(a, b)
            operacao = '+'
        elif opcao == '2':
            resultado = subtracao(a, b)
            operacao = '-'
        elif opcao == '3':
            resultado = multiplicacao(a, b)
            operacao = '×'
        elif opcao == '4':
            resultado = divisao(a, b)
            operacao = '÷'
        elif opcao == '5':
            resultado = potencia(a, b)
            operacao = '**'

        print(f"\nResultado: {a} {operacao} {b} = {resultado}")

        input("\nPressione Enter para continuar...")

menu()