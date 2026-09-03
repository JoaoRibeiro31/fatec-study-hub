# -*- coding: utf-8 -*-

import os, sys, time, math

a = -1
while a <= 0:
    a = float(input("\nInforme um valor maior que 0 para o primeiro valor: "))

b = float(input("Informe o segundo valor: "))
c = float(input("Informe o terceiro valor: "))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes são: {x1:.2f} e {x2:.2f}\n")
else:
   print("Não existem raízes reais para esses valores (Δ < 0).\n")
    
time.sleep(5)