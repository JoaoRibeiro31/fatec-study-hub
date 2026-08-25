'''
Meu primeiro programa em Python
'''

#####################################################

print ('Seja vem vindo ao meu primeiro programa!')

valor=float (input('Digite a nota que você quer: '))

print('Sua nota será então ',valor)

######################################################

nota1 =float (input('Digite a nota 1:'))
nota2 =float (input('Digite a nota 2:'))
print ( ( float (nota1) + float(nota2) ) / 2 )

######################################################

# Configura o idioma em Português
# -*- coding: utf-8 -*-

# usando módulos do python - Módulos são pacotes Phython
import os
import sys
import time

# apagar a tela
os.system('clear')

# variáveis e constantes 1° parte do quadro resumo
NOTA1=0
NOTA2=0
MEDIA=0

# 2° parte do quadro resumo é a leitura de dados
NOTA1 = float(input('Digite Nota1:'))
NOTA2 = float(input('Digite Nota2:'))

# 3° parte do quadro resumo são os cálculos e formulas etc
MEDIA = (NOTA1+NOTA2)/2

# 4° parte do quadro resumo é a exibição dos resultados saídas do programa
print('A média é:', MEDIA )
print('\n') # pula uma linha
time.sleep(5) # pausa de 5 segundos

sys.exit # comando de fim do programa

####################################################################

# Muda o idioma do script para utf-8 português

# -*- coding: utf-8 -*-

# usando módulos do python
import os 
import sys
import time

# apagar a tela
os.system('clear')

# variáveis e constantes 1° parte do quadro resumo
pi=3.14
resultado=0

# 3° parte do quadro resumo são os cálculos e formulas etc
resultado=10*pi

# 4° parte do quadro resumo é a exibição dos resultados saídas do programa
print('O resultado é:', resultado)

print('\n') # pula uma linha
time.sleep(5) # pausa de 5 segundos
sys.exit # comando de fim do programa




