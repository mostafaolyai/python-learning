import math
print("test")
print("AB" * 10)

student_count = 30
print(student_count)

# triple coute
message = """ Hi Smo
Software engineer
Ha Ha Ha"""
print(message)

print(len(message))

print(message[1])
print(message[-6])
print(message[1:5])
print(message[1:])
print(message[:-10])

# escape notation
txt = "python \n \" \' \\ \t programming"
print(txt)

# formatted string
first = "Coding   "
last = "is cool"

txt1 = first + " " + last
txt2 = f"{first} {last}"
print(txt1, txt2)

print(txt1, txt1.upper())  # return new result doesn't change main string (txt1)
print(txt1, txt1.lower())
print(first.strip(), first)  # remove spaces
print(first.rstrip(), first)  # remove right spaces
print(first.lstrip(), first)  # remove left spaces
print(first.find("Co"), first)
print(first.replace("Co", "Oc"), first)
print("z" in txt1, "z" not in txt2)

# complex
x = 2+3j

print(10 / 3)  # 3.33333333
print(10 // 3)  # 3
print(10 % 3)  # 1
print(10 ** 3)  # 1000
print(round(2.5))
print(round(2.3))
print(abs(-2.3))

print(math.ceil(4.5))


# ///////////////////////
x = input('x: ')  # input from consol
print(x)
print(float(x)+1)
print(type(x))
# print(x+1)//error

# compare with number of a and m ....
print(x == 1)
print('ali' > 'mohammad')
print('ali' > 'ALI')

if x == 5:
    print('x is 5')
else:
    print("x is not 5")

# new if
message = 'x is 5' if x == '5' else 'x is not 5'
print(message)

# or and
student = True
if not student and (x == 5 or x == 6):
    print('x is 5')
else:
    print("x is not 5")

# short circuit
a = True
b = True
c = False
print(c and a and b)
print(c or a or b)
