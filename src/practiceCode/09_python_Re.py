import re
x = "The rain in spain"
y = re.search("^The.*spain$", x)
print(y)