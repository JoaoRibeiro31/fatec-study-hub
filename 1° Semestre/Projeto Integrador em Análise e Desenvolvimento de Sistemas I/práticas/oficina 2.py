'''
Oficina 2
Tarefa/Avaliação Contínuada
Menu de Exercícios
'''

# Configura o idioma em Português
# -*- coding: utf-8 -*-

import os, sys, time, math

def exercicioA():
    base = input('\nInforme a base do triângulo: ')
    altura = input('Informe a altura do triângulo: ')
    area = (float(base) * float(altura)) / 2
    print(f'A área do triângulo é: {area:.2f}\n')
    time.sleep(5)
    input("Pressione ENTER para voltar ao menu...")

def exercicioB():
    tempo = input('\nInforme o tempo em segundos: ')
    distancia = float(tempo) * 340
    print(f'A distância do raio é: {distancia:.2f} metros\n')
    time.sleep(5)
    input("Pressione ENTER para voltar ao menu...")

def exercicioC():
    altura = input('\nInforme a altura em metros: ')
    TQ = math.sqrt((2 * float(altura)) / 9.8)
    print(f'O tempo de queda é: {TQ:.2f} segundos\n')
    time.sleep(5)
    input("Pressione ENTER para voltar ao menu...")

def exercicioD():
    perimetro = input('\nInforme o perímetro do círculo: ')
    diametro = float(perimetro) / math.pi
    raio = diametro / 2
    area = raio ** 2 * math.pi
    print(f'A área do círculo é: {area:.2f}\n')
    time.sleep(5)
    input("Pressione ENTER para voltar ao menu...")

# Menu principal
while True:
    os.system('clear')
    print('===== MENU DE EXERCÍCIOS =====')
    print('1 - Exercício A (Área do Triângulo)')
    print('2 - Exercício B (Distância de um Raio)')
    print('3 - Exercício C (Tempo de Queda Livre)')
    print('4 - Exercício D (Área do Círculo)')
    print('0 - Sair')
    print('==============================')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        os.system('clear')
        exercicioA()
    elif opcao == '2':
        os.system('clear')
        exercicioB()
    elif opcao == '3':
        os.system('clear')
        exercicioC()
    elif opcao == '4':
        os.system('clear')
        exercicioD()
    elif opcao == '0':
        print('Encerrando o programa...')
        time.sleep(2)
        sys.exit()
    else:
        print('Opção inválida! Tente novamente.\n')
        time.sleep(2)
