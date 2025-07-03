# symbol = '*'
# height = 8
# width = 8

# for i in range(height):
#     frontspace = ' '* int(width)
#     backspace = frontspace

#     if i < 4:
#         if i ==0:
#             print(symbol + " "*9 + symbol + (" " + symbol)*4)
#         elif i == 3:
#             print((symbol + " ")*4 + symbol + (" " + symbol)*5)
#         else :
#             print(symbol + frontspace + symbol)
    
#     else:
#         if i ==7:
#             print((symbol + " ")*4 +symbol + " "*9 + symbol)
#         else:
#             print(" " + frontspace + symbol + backspace + symbol )





symbol = '*'
height = 9
width = 9

for i in range(height):
    frontspace = ' '* int(width)
    backspace = frontspace

    if i < 5:
        if i ==0:
            print(symbol + " "*9 + symbol + (" " + symbol)*5)
        elif i == 4:
            print((symbol + " ")*5 + symbol + (" " + symbol)*5)
        else :
            print(symbol + frontspace + symbol)
    
    else:
        if i ==8:
            print((symbol + " ")*5 +symbol + " "*9 + symbol)
        else:
            print(" " + frontspace + symbol + backspace + symbol )


