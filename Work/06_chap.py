'''
                    6. Generators
'''
## 6.1 Iteration Protocol

a = 'hello'
for c in a: # Loop over characters in a
    print(c)

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # Loop over keys in dictionary
    print(k)
for k,v in b.items(): # Loop over keys and values in dictionary
    print(k,v)


## using hash function
    #https://stackoverflow.com/questions/4567089/hash-function-that-produces-short-hashes
import hashlib
import base64
plaintext1 ="long_namexyz_1234567892"
hash_result1 = hashlib.sha256(plaintext1.encode()).digest()[:16]
hash_result1
hash_result2 = hashlib.shake_256(plaintext1.encode()).hexdigest(4)
hash_result2
encoded_result = base64.b64decode(hash_result1).decode('UTF-8')  #base64.b64encode(hash_result1).decode("utf-8")
encoded_result 

encoded_result1 = encoded_result.decode("UTF-8")

