# -*- coding: utf-8 -*-

import os

while True:
    os.system("cls")
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    resultado = numero1 * numero2

    print(f"\nO resultado de {numero1} x {numero2} é = {resultado}")

    continuar = input("Deseja continuar? S/N: ").strip().lower()

    if continuar != 's':
        print("\nFim do programa!")
        break

    print("-" * 40)

