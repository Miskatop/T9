# T9 Encoder and Decoder in Python, V-0.3
#### T9 library allows use T9 keyboard combination to encoding and decoding string
#### T9 keyboard you can view in pushbutton nokia keyboard (Nokia 3310)

## Release Info
> Version-0.1
>> Basic Working code

> Version-0.2
>> Optimized Code And new encodeing type

> Version-0.3
>> Setup and Cythonize, add new chars

## Encode/Decode strings
#### this is exaple of encoded string : `4431525262269062725230`
#### this is decoden t9 string : `Hello world`

## How to install
```bash
sudo python3 setup.py
```

## How to use

```python 
from t9 import T9 # import T9

x = T9() # initializing T9 class
string = 'hello world' 
enc = x.encode('Hello world') # encoding string
print(f'this is exaple of encoded string : {enc}')
print(f'this is decoden t9 string : {x.decode(enc)}') # decoding encoded string
```

[My Facebook](https://www.facebook.com/King.of.the.wold.Misha/)

# Thank you for use the T9 library :wink:
