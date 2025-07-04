# rows = 6
# symbol = '*'
# j = 1
# for i in range (rows + 2):
#     if i <rows:
#         if i ==3:
#             spaces = rows - 2*i +1 
#             stars = 4 * i -3
#             print(" " * spaces + symbol * stars)

#             pass
#         else :
#             spaces = rows -i
#             stars = 2 * i -1
#             print(" " * spaces + symbol * stars)

#     else:
#         spaces = i - 2
#         stars = (i -3*j)
#         print(" " * spaces + symbol * stars)
#         j +=1



# inverted triangle
rows = 5 
symbol = "*"
print((symbol + " ") * rows) 

for i in range (1, rows):
    print((" " * i)+ (symbol + " ") * (rows - i))




## hollow traingle

# rows = 5
# symbol = "*"

# # Print the top of the triangle (base of original)
# print((symbol + " ")* rows)

# # Print the middle rows
# for i in range(1, rows - 1):
#     print(" " * i + symbol + " " * (2 * (rows - i - 1) - 1) + symbol)

# # Print the tip of the inverted triangle
# print(" " * (rows - 1) + symbol)
