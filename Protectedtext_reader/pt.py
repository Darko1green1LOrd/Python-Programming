from requests import get
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5
from base64 import b64decode
import re

class read_protectedtext(object):
    """
    Very useful sites :
    https://github.com/CogitoErgoCode/protectedtext-bruteforcer/tree/main
    https://cogitoergocode.github.io/protectedText/
    """
    def _decrypt(self, password, ciphertext):
        try:
            decoded    = b64decode(ciphertext)
            salt       = decoded[8:16]
            ciphertext = decoded[16:]
            key, iv    = self._key_derivation_evp(password, salt)
            decipher   = AES.new(key, AES.MODE_CBC, iv)
            decrypted  = decipher.decrypt(ciphertext)
            unpadded   = unpad(decrypted, AES.block_size)
            plaintext  = unpadded[:-128] #SHA512 (128-bytes)
            return plaintext.decode('utf-8').split("f47c13a09bfcad9eb1f81fbf12c04516e0d900e409a74c660f933e69cf93914e16bc9facc7d379a036fe71468bd4504f2a388a0a28a9b727a38ab7843203488c") #new page separator
        except:
            pass

    @staticmethod
    def _key_derivation_evp(password, salt, keySize=8, ivSize=4, iterations=1, hashAlgorithm=MD5):
        """
        If the total key and IV length is less than the digest length and MD5 is used then the derivation algorithm is compatible with PKCS#5 v1.5 otherwise a non standard extension is used to derive the extra data.
        https://www.openssl.org/docs/manmaster/man3/EVP_BytesToKey.html
        https://github.com/CryptoStore/crypto-js/blob/3.1.2/src/evpkdf.js
        https://gist.github.com/adrianlzt/d5c9657e205b57f687f528a5ac59fe0e
        """
        targetKeySize     = keySize + ivSize
        derivedBytes      = b""
        derivedWordsCount = 0
        block             = None
        hasher            = hashAlgorithm.new()
        while derivedWordsCount < targetKeySize:
            if block:
                hasher.update(block)

            hasher.update(password)
            hasher.update(salt)
            block  = hasher.digest()
            hasher = hashAlgorithm.new()

            for _ in range(1, iterations):
                hasher.update(block)
                block  = hasher.digest()
                hasher = hashAlgorithm.new()

            derivedBytes += block[: min(len(block), (targetKeySize - derivedWordsCount) * 4)]

            derivedWordsCount += len(block) / 4

        # Password & IV Tuple
        return derivedBytes[0: keySize * 4], derivedBytes[keySize * 4:]

    def get_text(self,link,password):
        page = get(f"https://www.protectedtext.com/{link}")
        if not page.ok:
            return None

        soup = BeautifulSoup(page.text, "html.parser")
        scripts = soup.find_all('script')
        for script in scripts:
            scriptString = str(script)
            if "ClientState" in scriptString:
                try:
                    regex = re.search(rf'"\/{link}",\s+"(.+)"', scriptString, re.I)
                    in_pass = bytes(password, 'utf-8')
                    return (self._decrypt(in_pass, bytes(regex.group(1), 'utf-8')))
                except AttributeError:
                    return None

pt_reader = read_protectedtext()
print(pt_reader.get_text("testsite_test","test"))
