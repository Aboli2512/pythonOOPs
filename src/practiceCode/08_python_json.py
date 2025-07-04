import json

# x = '{"name" : "Aboli", "age" : 25, "language" : "Python", "salary" : 1500000}'
# y = json.loads(x)
# print(y)
# print(y['name'])
# print(y['salary'])


a = {"name" : "Aboli", "age" : 25, "language" : "Python", "salary" : 1500000}
b = json.dumps(a)
print(b)
print(type(b))


{"name" : "Aboli", "age" : 25, "language" : "Python", "salary" : 1500000}


## JSON TO PYTHON ==== JSON.LOADS
## PYTHON TO JSON ==== JSON.DUMPS
