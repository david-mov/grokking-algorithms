def count_items(arr):
    def counter(arr, result):
        if not arr: return result # base case
        result += 1
        arr.pop()
        return counter(arr, result) # recursive case
    return counter(arr, 0)

print(count_items([1,2,3,4,5,6]))
