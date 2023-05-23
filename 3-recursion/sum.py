# python decorator smart_number can be omitted (I did it for fun)

'''import numbers
def smart_sum(func):
    def inner(arr, initial_value = 0):
        if not isinstance(arr, list):
            raise Exception("sum() must receive a list of numbers as first parameter")
        if initial_value and not isinstance(initial_value, numbers.Number):
            raise Exception("The initial value must be a number")
        if not len(arr):
            raise Exception("The list must have at least one item")
        if any(not isinstance(item, numbers.Number) for item in arr):
            raise Exception("All items in the list must be numbers")
        return func(arr, initial_value)
    return inner

@smart_sum'''
def sum(arr, result = 0):
    if (not arr): return result # base case
    return sum(arr, result+arr.pop()) # recursive case

print(sum([1,2,3,4]))