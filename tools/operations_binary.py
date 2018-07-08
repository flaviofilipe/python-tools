#!/usr/bin/bash
#coding: utf-8

'''
Dev by Capitan Duke
http://github.com/flaviofilipe/
'''

def bin_dec(num):
	num = str(num)[::-1] #Inverte os numeros
	result = 0
	valores = [1,2,4,8,16,32,64,128]
	for i in range(0, len(num)):
		calc = int(num[i])*valores[i]
		result = result + calc
	return(result)
		#print(str(i)+' - '+str(num[i]))

def dec_bin(num):
	result = ''
	while num//2 >= 1:	
		mod = num%2 #Verifica o mod
		num = num//2 #Divisao inteira
		result = result+str(mod) #Cria string

	result = result+str(num)
	return(result[::-1]) #Retorna string invertida


def opcoes(operation):

	if operation == 0:
		print('Até mais!!')
		exit
	elif operation == 1:
		#Binario em decimal
		num = int(input('Insira o numero 1 de até 8bits: '))
		print(bin_dec(num))
	elif operation == 2:
		#Decimal em binario
		num = int(input('Insira o numero 1 de até 8bits: '))
		print(dec_bin(num))
	elif operation == 3:
		#Soma
		num1 = int(input('Insira o numero 1 de até 8bits: '))
		num2 = int(input('Insira o numero 2 de até 8bits: '))

		soma = bin_dec(num1)+bin_dec(num2)
		print('{} + {} = {}'.format(num1, num2, dec_bin(soma)))
	elif operation == 4:
		#Subtracao
		num1 = int(input('Insira o numero 1 de até 8bits: '))
		num2 = int(input('Insira o numero 2 de até 8bits: '))
		
		sub = bin_dec(num1)-bin_dec(num2)
		print('{} - {} = {}'.format(num1, num2, dec_bin(sub)))
	else:
		print('comando nao identificado')


print('''
################################
#Operações com números binários#
################################
'''
	)

print('''
1 - Converter em decimal
2 - Converter em binário
3 - Soma de binários
4 - Subtração de binários
0 - Para sair
''')

value = 1
while value != 0:
	value = int(input('operacao: '))
	opcoes(value)
