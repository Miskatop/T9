#!/usr/bin/python3
from random import sample
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CRYPTER:
	def __init__(self, key="password"):
		password_provided = key
		password = password_provided.encode()
		salt = b'salt_'
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100,
			backend=default_backend()
		)

		key = base64.urlsafe_b64encode(kdf.derive(password)) 

		self._f = Fernet(key)

	def encode(self, data):
		return self._f.encrypt(bytes(data, "utf-8"))

	def decode(self, data):
		return self._f.decrypt(data).decode()


class T9:
	"""usage type :
	x = T9()
	string = 'hello world'
	enc = x.encode('Hello world')
	print(f'this is exaple of encoded string : {enc}')
	print(f'this is decoden t9 string : {x.decode(enc)}')"""
	structure = {
		1: ['0', '2', '3', '1', '7', '4', '5', '6', '9', '8', '%', '(', ')'],
		2: ['a', 'b', 'c', 'A', 'B', 'C', 'sp', '$', '!', '@', '^', '&', '*'],
		3: ['d', 'e', 'f', 'D', 'E', 'F', '_', '-', '=', '+', '~', '`', '<'],
		4: ['g', 'h', 'i', 'G', 'H', 'I', '>', '"', "'", ',', '.', '/', '\\'],
		5: ['j', 'k', 'l', 'J', 'K', 'L', '{', '}', '[', ']', '|', '՞'],
		6: ['m', 'n', 'o', 'M', 'N', 'O'],
		7: ['p', 'q', 'r', 's', 'P', 'Q', 'R', 'S'],
		8: ['t', 'u', 'v', 'T', 'U', 'V'],
		9: ['w', 'x', 'y', 'z', 'W', 'X', 'Y', 'Z'],
	}
	unknown = '*'
	_all_chars = []

	for c in structure.values():
		_all_chars.extend(c)

	def _encrypt(self, string): 
		res = ''
		for i in string:
			for c, v in self.structure.items():
				if i == ' ':
					i = 'sp'

				if i in v:
					res += str(c) + str(v.index(i)) + '|'
				elif not i in v and not i in self._all_chars:
					res += str(self.unknown) + str(i) + '|'
					break
		return res

	def _decrypt(self, string):
		res = ''
		for i in string.split('|'):
			decoded_char = None
			i = i if len(i) > 1 else False
			if i:
				key = i[0]
				if key == self.unknown:
					decoded_char = i[1:]
				else:
					decoded_char = self.structure[int(key)][int(i[1:])]

			if decoded_char == 'sp':
				decoded_char = ' '

			res += decoded_char if i else ''

		return res

	def encode(self, text, key=None, type=None):
		encrypted = ''

		if key:
			encrypted += self._encrypt(key) + '{k}'

		encrypted += self._encrypt(text)

		if type:
			return string(text,encrypted)
		else:
			return encrypted

	def decode(self, text, key=None):
		if not key and '{k}' in text:
			raise KeyError('string is protected by secure key')

		if '{k}' in text:
			key_hash = string.split('{k}')
			text = key_hash[1]
			code = self._decrypt(key_hash[0])

			if key != code:
				raise KeyError('Key is invalid')

		decrypted = ''

		decrypted += self._decrypt(text)

		return string(decrypted)

	def asString(self, text):
		stt = string(text)
		return stt

class STRINGER:
	def _spl_crypt(self, str_):
		PARTS = 2
		start = 0
		len_ = len(str_)
		parts = []
		for i in range(1, PARTS+1):
			end = int((len_/PARTS)*i)
			if i == PARTS:
				end = None
			parts.append(str_[start:end])
			start = end

		return str(parts[0])+"^|^"+str(parts[-1])


	def encrypt(self, string):
		encrypted = ""
		word_list = string.split(' ')
		indexes = {}
		keys = sample(word_list, len(word_list))

		for i, word in enumerate(word_list):
			indexes[word] = i

		for key in keys:
			encrypted += str(self._spl_crypt(key[::-1])) + "[||]" + str(indexes[key]) + "{||}"
		return encrypted


	def decrypt(self, string):
		wi_list = string.split("{||}")
		wi_2 = []
		for wi in wi_list.copy():
			if len(wi) > 0:
				wi_2.append(wi)

		result = ""
		sorted_ = [int(item.split("[||]")[-1]) for item in wi_2]
		sorted_.sort()

		for item in wi_2:
			text, i = item.split("[||]")
			text_ = text.split("^|^")[::-1]
			if len(text[0]) > 1 or len(text[1]) > 1:
				text_ = text_.reverse()

			text_ = text_[0][::-1] + text_[1][::-1]

			sorted_[int(i)] = text_

		for std in sorted_:
			result+=std+" "

		return result


class string:
	def __init__(self, text, enc=None):
		self._text = text
		self._enc = enc
		self._T9 = T9()

	def __str__(self):
		return self._text.replace('{k}', "")

	def decode(self, key=None):
		if self._enc:
			return self._T9.decode(self._enc, key)
		else:
			raise EOFError("string is not encoded")

	def encode(self, key=None):
		self._T9.encode(self._text, key, 1)
		self._enc = self._T9.encode(self._text, key)
		return self._enc

if __name__ == '__main__':
	import timeit
	from argparse import ArgumentParser

	t9 = T9()

	parser = ArgumentParser(description='T9 - encoder & decoder python version')

	parser.add_argument('-e', '--encode', default=None, help='string for encoding.' , type=str)
	parser.add_argument('-d', '--decode', default=None, help='string for decoding.' , type=str)
	parser.add_argument('-v', '--demo'  , default="Hello World !!!", help='Demo version of this app.', type=str)
	
	result = parser.parse_args()

	if not result.encode and not result.decode and not result.demo :
		parser.error('Enter the command line arguments')

	if result.encode:
		print('Encode: \n######## ->\n')
		print(t9.encode(result.encode))

	if result.decode:
		print('Decode: \n######## ->\n')
		print(t9.decode(result.decode))

	if result.demo:
		print('Demo encode: \n######## ->\n')
		enc = t9.encode(result.demo)
		print(enc)
		print('Demo decode: \n######## ->\n')
		print(t9.decode(enc))
