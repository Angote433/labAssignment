# Assignment 4 - Remove duplicates from a list, then sort and print
from collections import OrderedDict


# 1. Naive: loop and only add items not already in the new list
def remove_naive(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# 2. Using a condition with a list comprehension
def remove_conds(lst):
    result = []
    [result.append(item) for item in lst if item not in result]
    return result


# 3. Using a set
def remove_set(lst):
    return list(set(lst))


# 4. Using enumerate (keep an item only if this is its first position)
def remove_enum(lst):
    return [item for i, item in enumerate(lst) if item not in lst[:i]]


# 5. Using collections.OrderedDict
def remove_coll(lst):
    return list(OrderedDict.fromkeys(lst))


# Sort the list (after duplicates are removed) and print it
def print_list(lst):
    lst.sort()
    print(lst)


sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2, 7, 7, 9, 0, 0, 11, -5, -3]

print_list(remove_naive(sample_list))
print_list(remove_conds(sample_list))
print_list(remove_set(sample_list))
print_list(remove_enum(sample_list))
print_list(remove_coll(sample_list))