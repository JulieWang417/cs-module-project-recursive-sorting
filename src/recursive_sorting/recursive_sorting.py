# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arr = []
    # Your code here
    i = 0
    j = 0
    # Sort until one array is done
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]: 
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1
    # The other list might still have elements, so append them after
    while i < len(arrA):
        arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        arr.append(arrB[j])
        j += 1
    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    arrA = merge_sort(arr[:half])
    arrB = merge_sort(arr[half:])
    arr = merge(arrA,arrB)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return; 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1 
        else: 
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
              
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1 

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
  
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
