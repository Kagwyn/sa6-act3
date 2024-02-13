l1 = [1, 2, 3, 4]
l2 = [5, 4, 3, 8, 9]

intersection = list(filter(lambda x: x in l1, l2))
print(intersection)