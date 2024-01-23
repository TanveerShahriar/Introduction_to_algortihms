def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i 
    
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 5))
print(linear_search(arr, 6))