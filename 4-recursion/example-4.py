import math

def binary_search_recursive(lst, item):
    # validations
    if not isinstance(lst, list): raise Exception('The argument must be a list')
    if not lst: raise Exception('The list must have at least one element')

    def binary_search(lst, item, low ,high):
        mid = math.floor((low + high) / 2)
        guess = lst[mid]

        if guess == item: return mid # base case 1
        if low >= high: return None # base case 2

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

        return binary_search(lst, item, low, high) # recursive case
        
    return binary_search(lst, item, 0, len(lst)-1)

print(
    binary_search_recursive([1,3,5,7,9], 1), # index expected: 0
    binary_search_recursive([2,4,6,8], 6), # index expected: 2
    binary_search_recursive([1,2,3,4,5], 5), # index expected: 4
)