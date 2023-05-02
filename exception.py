try:
    x = int('zart')
except ValueError as e:
    # except (ValueError,ZeroDivisionError):
    print('zart is not a int', e, type(e))
except ZeroDivisionError:
    print('zero division')
else:
    print("when we don't have exception")
finally:
    print('finally')
#############################################################

try:
    file = open('test.txt')
except (ValueError, ZeroDivisionError):
    print('zart is not a int', e, type(e))
else:
    print("when we don't have exception")
finally:
    print('finally', file)
    file.close()
#############################################################

try:
    with open('test.txt') as file, open('test.txt') as file2:  # with automatically close file
        print(file)
except (ValueError, ZeroDivisionError):
    print('zart is not a int', e, type(e))
else:
    print("when we don't have exception")

########################## Custom Error ###################################


def calculate(age):
    if age <= 0:
        raise ValueError('zart')
    return 10/age


try:
    print(calculate(10), calculate(0))
except ValueError as e:
    print(e)
