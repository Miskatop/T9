#!/usr/bin/python3
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
