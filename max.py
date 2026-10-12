# Assignment 3 - Find the max value without using max()

# Method 1: recursion (compare first element with the max of the rest)
def max_recursion(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursion(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    return rest_max


# Method 2: pivot that splits the list in half
def max_pivot(lst):
    if len(lst) == 1:
        return lst[0]
    pivot = len(lst) // 2
    left_max = max_pivot(lst[:pivot])
    right_max = max_pivot(lst[pivot:])
    if left_max > right_max:
        return left_max
    return right_max


numbers = [4, 17, 9, 23, 1, 15, 8, 42, 30]

print("List:", numbers)
print("Max using recursion:", max_recursion(numbers))
print("Max using pivot    :", max_pivot(numbers))