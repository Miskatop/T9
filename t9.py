#!usr/bin/env python3
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

    def encode(self, string):
        res = ''
        for i in string:
            for c, v in self.structure.items():
                if i == ' ':
                    i = 'sp'
                if i in v:
                    res += str(c) + str(v.index(i)) + '|'
        return res

    def decode(self, string):
        res = ''
        for i in string.split('|'):
            i = i if len(i) > 1 else False
            if i:
                decoded_char = self.structure[int(i[0])][int(i[1:])]
            if decoded_char == 'sp':
                decoded_char = ' '
            res += decoded_char if i else ''

        return res

if __name__ == '__main__':
    import sys
    import timeit
    argv = sys.argv
    t9 = T9()

    start = timeit.default_timer()

    if '-e' in argv:
        print(t9.encode(argv[-1]))
    elif '-d' in argv:
        print(t9.decode(argv[-1]))
    else:
        enc = t9.encode('Hello World !!!')
        print(f'this is exaple of encoded string : {enc}')
        print(f'this is decoden t9 string : {t9.decode(enc)}')
    stop = timeit.default_timer()
    print('Time: ', stop - start)
