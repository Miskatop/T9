class T9{
	constructor(){
		this.structure = {
			1: ['0', '2', '3', '1', '7', '4', '5', '6', '9', '8', '%', '(', ')'],
			2: ['a', 'b', 'c', 'A', 'B', 'C', 'sp', '$', '!', '@', '^', '&', '*'],
			3: ['d', 'e', 'f', 'D', 'E', 'F', '_', '-', '=', '+', '~', '`', '<'],
			4: ['g', 'h', 'i', 'G', 'H', 'I', '>', '"', "'", ',', '.', '/', '\\'],
			5: ['j', 'k', 'l', 'J', 'K', 'L', '{', '}', '[', ']', '|', '՞'],
			6: ['m', 'n', 'o', 'M', 'N', 'O'],
			7: ['p', 'q', 'r', 's', 'P', 'Q', 'R', 'S'],
			8: ['t', 'u', 'v', 'T', 'U', 'V'],
			9: ['w', 'x', 'y', 'z', 'W', 'X', 'Y', 'Z'],
		};
	}
	_encrypt(str){
		let result='';
		let modeline;
		let char;
		let index;
		for(let _id=0; _id<str.length; _id++){
			char = str[_id]
			if (char == ' ') {
				char = 'sp';
			}
			for (let key in this.structure) {
				modeline = this.structure[key];
				index = modeline.indexOf(`${char}`);
				if (index != -1) {
					result += key.toString()+index.toString()+'|';
				}
			}
		}
		return result
	}
	_decrypt(source){
		let result='';
		let itemof;
		let char;
		let splited=source.split('|')
		splited.forEach(dec_string =>{
			if (dec_string != '') {
				itemof = dec_string.replace(dec_string[0], '').trim()
				char = this.structure[dec_string[0]][itemof];
				if (char == 'sp') {
					char = ' '
				}
				result += char;
			}
		})

		return result;
	}
	encode(content, key=null){
		let string = '';
		if (key && typeof(key) == 'string') {
			string += this._encrypt(key)+'{||}'
		}
		string+=this._encrypt(content)
		return string
	}
	decode(content, key=null){
		if (!key && 
			content.search("{||}") != -1) 
		{
			throw Error('Sorry !, string have a Secure key')
		}

		if (key) {
			content = content.split('{||}');
			if (key != this._decrypt(content[0])) {
				throw Error('Key is Invalid');
			}
			content = content[1]
		}

		return this._decrypt(content)
	}
}

t9 = new T9();
let encoded_string = t9.encode('Hello World', key='123456');
console.log(encoded_string)
console.log(t9.decode(encoded_string, key='123456'))
