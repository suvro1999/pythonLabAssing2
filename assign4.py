def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))
lst = [1, 2, 11, 14, 24, 26, 33]
print(find_missing(lst))
