strings = ['Hello', 'World', 'Bob', 'Yalooooo', 'Blu']

sorted_strings = sorted(strings, key=lambda x: (len(x), x))
print(sorted_strings)