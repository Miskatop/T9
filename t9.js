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
	encode(str){
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
	decode(source){
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
}

x = new T9();
let c = x.encode('Hello World !!!');
console.log(c)
console.log(x.decode(c))
