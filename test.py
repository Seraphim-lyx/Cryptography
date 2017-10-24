import asn1
from Crypto.Hash import SHA256
# from Crypto.Util import asn1
from binascii import hexlify
# message = 'SHA-256'.encode()
# print(hexlify(b'SHA-256'))
# encoder = asn1.Encoder()
# encoder.start()
# encoder.write(message)
# encoded_bytes = encoder.output()

# print(encoded_bytes)
# decoder = asn1.Decoder()
# decoder.start(encoded_bytes)
# tag, value = decoder.read()
# print(value)

# test = asn1.DerOctetString('asdfasdsfsa'.encode())
# t = test.encode()
# for i in t:
#     print(hex(i))
message = 'To be encrypted'
h = SHA.new(message)


cipher = PKCS1_v1_5.new(key)
ciphertext = cipher.encrypt(message + h.digest())
