#!usr/bin/env python3
class T9:
	"""usage type :
	x = T9()
	string = 'hello world'
	enc = x.encode('Hello world')
	print(f'this is exaple of encoded string : {enc}')
	print(f'this is decoden t9 string : {x.decode(enc)}')"""
	structure = {
		1:[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
		2:['a', 'b', 'c', 'A', 'B', 'C', 'sp'],
		3:['d', 'e', 'f', 'D', 'E', 'F'],
		4:['g', 'h', 'i', 'G', 'H', 'I'],
		5:['j', 'k', 'l', 'J', 'K', 'L'],
		6:['m', 'n', 'o', 'M', 'N', 'O'],
		7:['p', 'q', 'r', 's', 'P', 'Q', 'R', 'S'],
		8:['t', 'u', 'v', 'T', 'U', 'V'],
		9:['w', 'x', 'y', 'z', 'W', 'X', 'Y', 'Z'],
	}
	def encode(self, string):
		res = ''
		for i in string:
			for c,v in self.structure.items():
				if i == ' ':
					i = 'sp'
				if i in v:
					res += str(c)+str(v.index(i))
		return res

	def decode(self, string):
		res = ''
		str_list = []
		while len(string) != 0:
			str_list.append(string[:2])
			string = string[2:]

		for i in str_list:
			decoded_char = self.structure[int(i[0])][int(i[-1])]
			if decoded_char == 'sp':
				decoded_char = ' '
			res+=decoded_char

		return res

if __name__ == '__main__':
	import sys
	argv = sys.argv
	t9 = T9()
	if '-e' in argv :
		print(t9.encode(argv[-1]))
	elif '-d' in argv :
		print(t9.decode(argv[-1]))
	else:
		enc = t9.encode('Hello world')
		print(f'this is exaple of encoded string : {enc}')
		print(f'this is decoden t9 string : {t9.decode(enc)}')