![Logo](https://github.com/Miskatop/T9/blob/master/T9Logo.png?raw=true)
# Encoder and Decoder for Python, V-0.3
#### T9 library allows use T9 keyboard combination to encoding and decoding string
#### T9 keyboard you can view in pushbutton nokia keyboard (Nokia 3310)

## T9 - Encode/Decode strings
#### this is exaple of encoded string : `4431525262269062725230`
#### this is decoded t9 string : `Hello world`

## STRINGER - Encode/Decode strings
#### this is exaple of encoded string : `ol^|^leH[||]0{||}dl^|^roW[||]1{||}`
#### this is decoded t9 string : `Hello world`

## CRYPTER - Encode/Decode strings
#### this is exaple of encoded string : `gAAAAABgD8sRN5k2dFMDW4YCqclCV5HFN2bQV2TR5lVy0LA2ROAt_tRJB6Oic1dLinMPs_3h8tGORtGi1IrQFEbHICYjF4Op0g==`
#### this is decoded t9 string : `Hello world`

## How to use in Python3.7.*

### T9 - crypter`
```python 
from t9 import T9 # import T9

x = T9() # initializing T9 class
string = 'hello world' 
enc = x.encode('Hello world') # encoding string
print(f'this is exaple of encoded string : {enc}')
print(f'this is decoden t9 string : {x.decode(enc)}') # decoding encoded string
```

### STRINGER - crypter`
```python 
from t9 import STRINGER # import STRINGER()

x = STRINGER() # initializing STRINGER class
string = 'hello world' 
enc = x.encode('Hello world') # encoding string
print(f'this is exaple of encoded string : {enc}')
print(f'this is decoden STRINGER string : {x.decode(enc)}') # decoding encoded string
```

### CRYPTER - crypter`
```python 
from t9 import CRYPTER # import CRYPTER()

x = CRYPTER() # initializing CRYPTER class
string = 'hello world'
enc = x.encode('Hello world') # encoding string
print(f'this is exaple of encoded string : {enc}')
print(f'this is decoden CRYPTER string : {x.decode(enc)}') # decoding encoded string
```

### base64 - crypter`
```python 
from t9 import base64 # import base64

encoded = base64.encodebytes(b"Hello world")

print(encoded.decode())
print(base64.decodebytes(encoded).decode())

```


[My Facebook](https://www.facebook.com/King.of.the.wold.Misha/)

# Thank you for use the T9 library :wink:
