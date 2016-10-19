## Installation

pip install rc4-python3

## Usage

```
from rc4 import decrypt, encrypt

data = 'some str'
key = 'some psw'

encrypted = encrypt(data, key)
assert decrypt(encrypted, key) == data

# for more
# dir(rc4)
```

## Command line tools

```
pyrc4 encrypt somedata somekey
pyrc4 decrypt somedata somekey
```
