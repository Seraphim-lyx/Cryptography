from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import os
counter = os.urandom(16)
print([hex(i) for i in counter])