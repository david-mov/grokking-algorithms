# Quicksort algorithm 
# that choose the rightmost element as the pivot but partitions the array to place it in the middle 

def partition(lst, low, high):
    i = low # Pointer to the index that will separate the elements smaller and greater than the pivot
    pivot = lst[high] # Choose the rightmost element as pivot

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        # Put all elements smaller than pivot to the left of i
        if lst[j] <= pivot:
            lst[j], lst[i] = lst[i], lst[j] # If the current element is less than or equal to the pivot, swap it with the i element
            i += 1 # Increase the pointer i by 1
   
    lst[i], lst[high] = lst[high], lst[i] # Swap the pivot with the i element so the pivot is in the correct position
    return i # Return the position from where partition is done

def qsort(lst, low, high):
    if low < high: # Base case
        partition_idx = partition(lst, low, high)
        left = qsort(lst, low, partition_idx-1)
        right = qsort(lst, partition_idx+1, high)

# Driver Code
if __name__ == '__main__':
    lst_a = [7,1,8,3,9]
    lst_b = [1,8,3,9,5]

    qsort(lst_a, 0, len(lst_a)-1)
    qsort(lst_b, 0, len(lst_b)-1)

    print(
        lst_a,
        lst_b
    )