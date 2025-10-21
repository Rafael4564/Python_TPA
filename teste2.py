# -*- coding: utf-8 -*-

import os

while True:
    os.system("cls")
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    operacao = float(input("Digite a sua operação: "))

    if operacao == '*':

    resultado1 = numero1 * numero2

    print(f"\nO resultado de {numero1} x {numero2} é = {resultado1}")

    if operacao == '/':

    resultado2 = numero1 / numero2

    print(f"\nO resultado de {numero1} / {numero2} é = {resultado2}")

    continuar = input("Deseja continuar? S/N: ").strip().lower()

    if continuar != 's':
        print("\nFim do programa!")
        break

    print("-" * 40)
