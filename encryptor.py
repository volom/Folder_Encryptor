#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:51:34 2021

@author: volom
"""

from cryptography.fernet import Fernet
import base64
import os

while True:
    folder_path = input("Enter path to folder where you want to encrypt files ")
    print("Is it the right directory you have chosen?")
    for i in os.listdir(folder_path):
        print(i)
    confirm = input('[y/n]?')
    if confirm.lower() == 'y':
        break
    else:
        continue

while True:
    try:
        while True:
            print("Password must contain special characters, only Latin, no spaces")
            init_key = input("Set password to encrypt files ---> ")
            check_password = input("Enter password again to check ---> ")
            if init_key == check_password:
                break
            else:
                print("Check failed!")
                continue
            
        key = bytes(str(init_key*31)[:31], 'utf8')
        key = base64.urlsafe_b64encode(key)
        key = bytes(init_key[0]+str(key)[2:-2], 'utf8')
        
        f = Fernet(key)
    except Exception as e:
        if str(e) == 'Incorrect padding':
            print("Unsuitable symbols in the password")
    else:
        break

# Encrypt


list_files = []
for (dirpath, dirnames, filenames) in os.walk(folder_path):
    list_files += [os.path.join(dirpath, file) for file in filenames]

for file in list_files:
    with open(file, 'rb') as original_file:
        original = original_file.read()
        encrypted = f.encrypt(original)
    with open (file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        
print(f"The encryption was done successfuly. Save your password to decrypt - |{init_key}|")




