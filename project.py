import hashlib
n = input("enter a string:")
salt = "a23s4d5r"
F=(n+salt)
result = hashlib.md5(F.encode())
print(result)
s=hashlib.sha256(n.encode())
print(s.hexdigest())
T=hashlib.sha384(n.encode())
print(T.hexdigest())
I=hashlib.sha512(n.encode())
print(I.hexdigest())
a_dict = {s:n,T:s}
items = a_dict.items()
items
for item in a_dict.items():
    print(item)