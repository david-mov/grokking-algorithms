def find_max_recursive(arr):
    if len(arr) < 2: return arr[0] if arr else None
    def find_max(arr, max_val = float('-inf')):
        if not arr: return max_val # base case
        max_val = arr[0] if arr[0] > max_val else max_val
        return find_max(arr[1:], max_val) # recursive case
    return find_max(arr)

print(
    find_max_recursive([2,7,3,9,1]), # result: 9
    find_max_recursive([1,3]), # result: 3
    find_max_recursive([3,6,5,2,7]), # result: 7
    find_max_recursive([]), # result: None
    find_max_recursive([4]) # result: 4
)