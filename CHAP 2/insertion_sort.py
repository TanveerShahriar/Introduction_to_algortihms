# Time Complexity:

# Best  Case : O(n)
# Avg   Case : O(n^2)
# Worst Case : O(n^2)

# Space Complexity: O(1) (Always)

# Insertion sort is a stable sorting algorithm

def insertion_sort(arr, reverse = False):
    for i in range(1, len(arr)):
        temp = arr[i]
        
        idx = i - 1
        while idx >= 0 and ((reverse and arr[idx] < temp) or (not reverse and arr[idx] > temp)):
            arr[idx + 1] = arr[idx]
            idx -= 1
        
        arr[idx + 1] = temp

def insertion_sort_recursive(arr, i = 1, reverse = False):
    if len(arr) == i:
        return
    
    temp = arr[i]
    idx = i - 1
    
    while idx >= 0 and ((reverse and arr[idx] < temp) or (not reverse and arr[idx] > temp)):
        arr[idx + 1] = arr[idx]
        idx -= 1
    
    arr[idx + 1] = temp 
    
    insertion_sort_recursive(arr, i + 1, reverse)
    

arr = [10, 9, 8, 7, 6, 5]
insertion_sort(arr)
print(arr)
insertion_sort(arr, reverse = True)
print(arr)  

arr = [10, 9, 8, 7, 6, 5]
insertion_sort_recursive(arr)
print(arr)
insertion_sort_recursive(arr, reverse = True)
print(arr)  