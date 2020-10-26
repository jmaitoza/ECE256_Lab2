#!/usr/bin/env python3
import os
import sys
shift = int(sys.argv[1])

ciptext = open("ciphertext_file.txt", "r")
ctxt = ciptext.read()

decrypted = " "

for c in ctxt:
    c_uni = ord(c)
    c_index = ord(c) - ord(" ")
    new_index = (c_index - shift) % 94

    new_uni = new_index + ord(" ")
    new_char = chr(new_uni)

    decrypted = decrypted + new_char



print("Cipher text: ", ctxt)
print("Decrypted text: ", decrypted)
