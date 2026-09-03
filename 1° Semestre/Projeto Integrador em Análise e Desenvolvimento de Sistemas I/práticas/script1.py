# -*- coding: utf-8 -*-
import os
import time
import sys

sexo = ''
msg = ''

os.system('cls')

sexo = input('Digite o sexo M/F: ')

if sexo == 'F':
 msg = 'Trata-se de uma Mulher'

else:
 msg = 'Trata-se de um Homem'

# os.system('cls')

print (msg)
time.sleep(5)
sys.exit # sai do programa