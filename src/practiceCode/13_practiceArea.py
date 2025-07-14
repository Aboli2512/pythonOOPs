# import math
# # initialise class
# class Area:
#     def __init__(self, shape):
#         self.shape = shape
        # self.side1 = side1
        # self.side2 = side2
        # self.side3 = side3
# # calculate area
#     def CalculateArea(self):
#         # match self.shape:
#         #     case 'Circle':
#         #         return (math.pi) * self.side**2
#         #     case 'Rectangle':
#         #         return self.side1*self.side1
#         #     case 'Square':
#         #         return self.side1**2
#         #     case 'EquilateralTraingle':
#         #         return math.sqrt(3)/4 * self.side1**2
#         #     case 'RightAngleTraingle':
#         #         return 0.5 * self.side1 * self.side2
#         #     case _:
#         #         pass
#         return 23
    
# a = Area('circle')
# variable = a.CalculateArea()
# if variable

myDict = {}
myList1 = ['apple' , 'banana', 'cherry', 'kiwi']
myList2 = ['red', 'yellow', 'orange', 'green']
a = tuple(myList1)
b = tuple(myList2)

# keys = myList1
# values = myList2

# myDict = dict(zip(keys, values))
# print(myDict)



# myDict = {
#     myList1[0] : myList2[0],
#    myList1[1] : myList2[1],
#     myList1[2] : myList2[2]
# }

# print(myDict)
# print(myDict[myList1[1]])
# myDict = {}
# myDict[myList1[0]] = myList2[0]
# myDict[myList1[1]] = myList2[1]
# myDict[myList1[2]] = myList2[2]

# for i in range(len(myList1)):
#     myDict[myList1[i]] = myList2[i]
# print(myDict)


for i in range (4):
    keys = a
    values = b
    myDict.update({keys : values})
print(myDict)