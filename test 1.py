def all_uniqur(a):
    return True if len(a) == len(set(a)) else False

print(all_uniqur([1, 2, 3, 4, 6, 1]))
print(all_uniqur([1, 2, 3, 4, 6, 9]))