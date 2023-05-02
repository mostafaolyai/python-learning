# for
for number in range(4):
    print(number)


# for number in range(4):
#     print(number+1 * '.')  # error chon taghadom * bishtar az + hast,
    # 1*'.' => number+'.' => error

for number in range(1, 4):
    print((number+1) * '.')

successful = True
for number in range(4):
    if successful:
        print('success')
        break

#
for number in 'Mostafa':
    print(number)

# WHILE
num = 100
while num > 0:
    print(num)
    num //= 2
print('exit')
