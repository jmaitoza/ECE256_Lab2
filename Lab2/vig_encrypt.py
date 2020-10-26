#!/usr/bin/env python3
import os
import sys

plaintext = open("plaintext.txt", "r") #opens plaintext file
message = plaintext.read().strip()

msg_len = len(message)


keyword = sys.argv[1]    
encrypted = ""
cnt = 0
#set keyword to length of message
def find_key_len(keyword, msg_len):
    return (keyword * (msg_len // len(keyword) + 1)) [:msg_len]

msg_key = find_key_len(keyword, msg_len)

for c in message:
    k_uni = ord(msg_key[cnt])
    k_index = ord(msg_key[cnt]) - ord(" ")
    
    c_uni = ord(c)
    c_index = ord(c) - ord(" ")   
    new_index = (c_index + k_index) % 94
    
    new_uni = new_index + ord(" ")
    new_char = chr(new_uni)
    encrypted = encrypted + new_char
    cnt += 1        

print("Plain text: ", message)
print("Encrypted text: ", encrypted)
ciptext = open("ciphertext_file.txt", "r+") #opens ciphertext file
contents = ciptext.read().split("\n") #following code checks if file is empty and if not empties the$
ciptext.seek(0)
ciptext.truncate()
ciptext.write(encrypted) #writes encryped text to file
plaintext.close() #closes files
ciptext.close()
