from Crypto import Random
from Crypto.Cipher import AES
from os import listdir
from os.path import isfile, join

import os
import re, uuid
import os.path


class Encrpy:
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def create_master(self):
        f = open("master.enc", 'rb')
        f.close()

    def add_entry_to_master(self, password, key):
        master_key = ':'.join(re.findall('..', '%012x' % uuid.getnode()))  # MAC Address of the current pc
        entry = password + " " + key + "\n"

        iv = Random.new().read(AES.block_size)
        cipher = AES.new(master_key, AES.MODE_CBC, iv)
        enc = iv + cipher.encrypt(entry)
        with open("master.enc", 'rb') as fo:
            fo.write(enc)

    def encrypt(self, message, password, key):
        message = self.pad(message)


    def decrypt(self, ciphertext, password, key):

    def encrypt_file(self, file_name):

    def decrypt_file(self, file_name):
