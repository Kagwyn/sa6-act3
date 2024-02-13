from functools import reduce

numbers = [5, 3, 2, 1, 4, 4]

max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(max_val)