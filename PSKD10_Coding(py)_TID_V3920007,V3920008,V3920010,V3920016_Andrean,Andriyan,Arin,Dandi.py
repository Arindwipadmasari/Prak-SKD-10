# encryption
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

data = "Andrean Dandi Arin Tatak"

# 8 byte block
key = b'yesnoare'

# Menetapkan panjang data yang akan dienkripsi
BLOCK_SIZE = 32

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

print("Hasil enkripsi : ",encrypted_text)

# decryption
# 8 byte block
key = b'yesnoare'
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print("Hasil deskripsi : ",decrypted_text.decode())
