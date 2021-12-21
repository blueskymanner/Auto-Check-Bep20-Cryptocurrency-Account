from web3 import HTTPProvider, Web3
from coincurve import PublicKey
from sha3 import keccak_256
from binascii import unhexlify
import sys
import random
w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/99ccf60270394712a52e873ab72c5716'))

cnt = 0
bits = 16 ** 63 #random.getrandbits(256)
bits_hex = hex(bits)
key = bits_hex[2:]
key = key.zfill(64)
print(key)
  
while 1:
  bits_hex = hex(bits)
  bits = bits + 1
  key = bits_hex[2:]
  key = key.zfill(64)
  print(key)
  if cnt > 1000000:
    w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/99ccf60270394712a52e873ab72c5716'))

  cnt = cnt + 1
      
  try:
    key = key.strip()
    
    public_key = PublicKey.from_valid_secret(unhexlify(key)).format(compressed=False)[1:]
    address = keccak_256(public_key).digest()[-20:]
    address = '0x' + address.hex()
    address = w3.toChecksumAddress(address)
    
    balance = w3.fromWei(w3.eth.get_balance(address), 'ether')
    if balance > 0:
      out_file = open("output.txt", "a")
      out_file.write(key + " | " + str(balance) + "ETH\n")
      out_file.close()
      print(address)
      

  except Exception as e:
    print(e)
    cnt = cnt
