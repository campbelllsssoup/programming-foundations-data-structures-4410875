def has_unique_characters(data):
    fset = frozenset(list(data))
    return True if len(fset) == len(list(data)) else False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))

