#!/usr/bin/env python

import string
import random
import sys
 
#genere une variable string de size characteres
def generate_data(size):
	data = ""
	for x in range(size):
		data += random.choice(string.hexdigits)
	return data


#applique BER sur le string binaire
def applyBERonbinarybyte(BER,byte_bin):
	newbyte_bin = ""
	BER = 0.2
	for bit in byte_bin:
		probability = random.random()
		if probability <= BER:
			print("erreur")
			if bit == '0':
				bit = '1'
			elif bit == '1':
				bit = '0'
		newbyte_bin += bit
	return newbyte_bin
	


data = generate_data(1000)
data = "ok"
data_bytes = bytes(data, 'utf-8')
print(data_bytes)
for byte in data_bytes:
	baa = bytes(byte)
	print(byte)
	byte_bin = bin(byte)
	print(byte_bin)
	byte_bin = byte_bin[2:]
	byte_bin = applyBERonbinarybyte(0.5,byte_bin)
	str_bin = "0b"
	byte_bin = str_bin+byte_bin
	print(byte_bin)
	print(int(byte_bin,2))
print(data_bytes)












