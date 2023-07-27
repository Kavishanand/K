import json
a=[1,2,3,4,5,6]

b=json.dumps(a)
print(type(b))

c=json.loads(b)
print(type(c))

