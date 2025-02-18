from requests import post,get
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

protectedtext_site = "/testsite_test"

pt_site = get(f"https://www.protectedtext.com{protectedtext_site}")
pt_text = pt_site.text
startpoint = pt_text.find(protectedtext_site)-1
endpoint = pt_text.find('=="')+3
var = f'[{pt_text[startpoint:endpoint].replace(" ","")}]'
data = eval(var)
encrypted_site = hashlib.sha512(data[0].encode())
data_to_remove = encrypted_site.hexdigest()

test = AESCipher("test")

output = test.decrypt(data[1])
while True:
    try:print(eval(input("input: ")))
    except Exception as e:print(e)
