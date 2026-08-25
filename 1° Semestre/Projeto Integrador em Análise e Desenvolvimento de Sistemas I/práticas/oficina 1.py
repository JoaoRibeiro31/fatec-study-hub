# Coloca o idioma em português
# -*- coding: utf-8 -*-

# usando módulos do python
import os, sys, time

# apagar a tela
os.system('clear')  # no Windows pode usar 'cls'

while True:
    print("Escolha uma opção:")
    print("1 - Exercício A")
    print("2 - Exercício C")
    print("3 - Exercício D")
    print("4 - Exercício E")
    print("5 - Exercício H")
    print("0 - Sair")

    opcao = input("Digite o número da opção: ")

    ####################################################################################

    if opcao == "1":
        print("Rodando exercício A...")
        # 1 parte - variáveis
        CEL=0
        FAR=0

        # 2 parte - leitura
        CEL=float(input("Digite o valor da temperatura em Celsius: "))

        # 3 parte - cálculos
        FAR=(CEL * 9 + 160)/5

        # 4 parte - saída
        print("O valor da temperatura em Fahrenheit é:", round(FAR,2))

        print('\n')
        time.sleep(5)
        input("Pressione ENTER para voltar ao menu...")


    ####################################################################################

    elif opcao == "2":
        print("Rodando exercício C...")
        # 1 parte - variáveis
        raio=0
        altura=0
        volume=0
        pi=3.14

        # 2 parte - leitura
        raio=float(input("Informe o raio da lata: "))
        altura=float(input("Informe a altura da lata: "))

        # 3 parte - cálculos
        volume=pi*(raio**2)*altura

        # 4 parte - saída
        print("O volume da lata é:", round(volume,2))

        print('\n')
        time.sleep(5)
        input("Pressione ENTER para voltar ao menu...")


    ####################################################################################

    elif opcao == "3":
        print("Rodando exercício D...")
        # 1 parte - variáveis
        tempo=0
        velocidade=0
        distancia=0
        litros_usados=0
        consumo=12

        # 2 parte - leitura
        tempo=float(input("Informe o tempo gasto na viagem (horas): "))
        velocidade=float(input("Informe a velocidade média (km/h): "))

        # 3 parte - cálculos
        distancia=tempo*velocidade
        litros_usados=distancia/consumo

        # 4 parte - saída
        print("Velocidade média:", velocidade)
        print("Tempo gasto:", tempo)
        print("Distância percorrida:", distancia)
        print("Litros de combustível usados:", round(litros_usados,2))

        print('\n')
        time.sleep(5)
        input("Pressione ENTER para voltar ao menu...")


    ####################################################################################

    elif opcao == "4":
        print("Rodando exercício E...")
        # 1 parte - variáveis
        valor=0
        taxa=0
        tempo=0
        prestacao=0

        # 2 parte - leitura
        valor=float(input("Informe o valor da prestação: "))
        taxa=float(input("Informe a taxa de juros (%): "))
        tempo=int(input("Informe o tempo de atraso (meses): "))

        # 3 parte - cálculos
        prestacao=valor+(valor*taxa/100)*tempo

        # 4 parte - saída
        print("O valor da prestação em atraso é:", round(prestacao,2))

        print('\n')
        time.sleep(5)
        input("Pressione ENTER para voltar ao menu...")


    ####################################################################################

    elif opcao == "5":
        print("Rodando exercício H...")
        # 1 parte - variáveis
        comprimento=0
        largura=0
        altura=0
        volume=0

        # 2 parte - leitura
        comprimento=float(input("Informe o comprimento da caixa: "))
        largura=float(input("Informe a largura da caixa: "))
        altura=float(input("Informe a altura da caixa: "))

        # 3 parte - cálculos
        volume=comprimento*largura*altura

        # 4 parte - saída
        print("O volume da caixa é:", round(volume,2))

        print('\n')
        time.sleep(5)
        input("Pressione ENTER para voltar ao menu...")


    ####################################################################################

    elif opcao == "0":
        print("Saindo do programa...")
        time.sleep(2)
        sys.exit()

    else:
        print("Opção inválida! Por favor, insira um número válido.\n")
        time.sleep(2)
        os.system('clear')
