from t9 import T9, STRINGER, CRYPTER, base64

print("\nT9 --------->\n")

t9 = T9()

string = t9.asString("Hello ;")

print(string.encode())

print(string.decode())

print("\nSTRINGER --------->\n")

s = STRINGER()

encrypted = s.encrypt("Hi Mike How Are You ?")

print(encrypted)

print(s.decrypt(encrypted))

print("\nCrypter --------->\n")

c = CRYPTER()

enc = c.encode("Hello")

print(enc)
print(c.decode(enc))

print("\nBase64 --------->\n")

encoded = base64.encodebytes(b"Sophie")

print(encoded.decode())
print(base64.decodebytes(encoded).decode())