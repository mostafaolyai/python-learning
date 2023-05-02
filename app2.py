# function
def greet():
    print('hi everyone')


greet()


def greet2(first_name, last_nme):
    print(f'hi {first_name} {last_nme}')


greet2('mostafa', 'olyai')


def greet3(first_name, last_nme):
    return f'hi {first_name} {last_nme}'


print(greet3('mostafa', 'olyai'))

# write file
message = greet3('mostafa', 'olyai')
file = open('test.txt', 'w')
file.write(message)

# keyword arguments
print(greet3(last_nme='mostafa', first_name='olyai'))


def greet4(first_name, last_name='olyai'):  # optional put on the last
    return f'hi {first_name} {last_name}'


print(greet4('mosi'))


def greet4(a, b, c):
    print(a*b*c)


greet4(1, 2, 4)


def greet5(*nums):
    result = 1
    for num in nums:
        result = num*result
    print(result)


greet5(1, 2, 4)


def user(**user):
    print(user)


user(id=1, name='mosi')


def user(*user):
    print(user)


user(id=1, name='mosi')
