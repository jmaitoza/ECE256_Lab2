#!/usr/bin/env python3
import os
import sys
shift = int(sys.argv[1])

plaintext = open("plaintext.txt", "r") #opens plaintext file
plntxt = plaintext.read().strip()

encrypted = ""


for c in plntxt:
#	if not c.isalpha():
	#	pass
	#	continue
	#if c.isupper(): # checks if plain text is capital letters
		c_uni = ord(c) #turns char into unicode
		c_index = ord(c) - ord(" ") #creates new index
		new_index = (c_index + shift) % 94 #shifts each char based on shift value

		new_uni = new_index + ord(" ") #converts unicode back to char
		new_char = chr(new_uni)

		encrypted = encrypted + new_char # creates new string based on encrypted characters
#	else:
#		c_uni = ord(c)
#		c_index = ord(c) - ord("a")
#		new_index = (c_index + shift) % 26
#
#		new_uni = new_index + ord("a")
#		new_char = chr(new_uni)
#
#		encrypted = encrypted + new_char

print("Plain text: ", plntxt)
print("Encrypted text: ", encrypted)
ciptext = open("ciphertext_file.txt", "r+") #opens ciphertext file
contents = ciptext.read().split("\n") #following code checks if file is empty and if not empties the file to write new text to it
ciptext.seek(0)
ciptext.truncate()
ciptext.write(encrypted) #writes encryped text to file
plaintext.close() #closes files
ciptext.close()


