####################################### time ####################
from timeit import timeit
code1 = """

def calculate(age):
    if age <= 0:
        raise ValueError('zart')
    return 10/age


try:
    calculate(0)
except ValueError as e:
    pass #without print or exec code just pass here
"""
code2 = """

def calculate(age):
    if age <= 0:
        return None
    return 10/age

calculate(10)
"""
print('code1', timeit(code1, number=10000))
print('code2', timeit(code2, number=10000))
