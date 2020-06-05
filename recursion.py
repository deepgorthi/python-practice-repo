#!/usr/bin/env python3

def sum_recursion(input_array):
    if len(input_array) == 1:
        return input_array[0]
    else:
        return sum_recursion(input_array[1:]) + input_array[0]

def count_items(input_array):
    if input_array is None:
        return 0
    else:
        return 1 + count_items(input_array[1:])



print(sum_recursion([1,2,3,4,5]))
print(count_items([1,2,3,4,5,10]))

