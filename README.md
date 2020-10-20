# T9 Encoder and Decoder in Python, V-0.3
#### T9 library allows use T9 keyboard combination to encoding and decoding string
#### T9 keyboard you can view in pushbutton nokia keyboard (Nokia 3310)

## Release Info
> Version-0.1
>> Basic Working code

> Version-0.2
>> Optimize Code And new encodeing type

> Version-0.3
>> Create Setup.py for installing in python
>> Cythonize
>> Add new chars

> Version-0.4
>> Add javascript encoder
>> Add key mode to scripts ( 20.10.2020 - Only python )

## Encode/Decode strings
#### this is exaple of encoded string : `44|31|52|52|62|26|94|62|72|52|30|`
#### this is decoden t9 string : `Hello world`

## How to install
```bash
sudo python3 setup.py
```

## How to use

```js
t9 = new T9(); // initializing T9 class
let encoded_string = t9.encode('Hello World !!!'); // encoding string
console.log(encoded_string)
console.log(t9.decode(encoded_string)) // decoding encoded string
```

```python 
from t9 import T9 # import T9

x = T9() # initializing T9 class
string = 'hello world' 
enc = x.encode('Hello world') # encoding string
print(f'this is exaple of encoded string : {enc}')
print(f'this is decoden t9 string : {x.decode(enc)}') # decoding encoded string
```

## You can inject key to string ( Only Python version )
```python
from t9 import T9 # import T9

x = T9() # initializing T9 class
string = 'hello world' 
enc = x.encode('Hello world', key = '123456') # encoding string
print(f'this is exaple of encoded string : {enc}')
dec = x.decode(enc, key = '123456')
print(f'this is decoden t9 string : {dec}') # decoding encoded string
```
[My Facebook](https://www.facebook.com/King.of.the.wold.Misha/)

# Thank you for use the T9 library :wink:
