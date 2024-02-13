from functools import reduce

number = 573

sum_digits = reduce(lambda x, y: int(x) + int(y), str(number))
print(sum_digits)