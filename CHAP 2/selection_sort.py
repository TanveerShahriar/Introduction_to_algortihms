# Time Complexity: O(n^2) (Always)

# Space Complexity: O(1) (Always)

def selection_sort_unstable(arr, reverse = False):
    size = len(arr)
    
    for i in range(size - 1):
        min_idx = i
        for j in range(i+1, size):
            if (not reverse and arr[j] < arr[min_idx]) or (reverse and arr[j] > arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
def selection_sort_stable(arr, reverse = False):
    size = len(arr)
    
    for i in range(size - 1):
        min_idx = i
        for j in range(i+1, size):
            if (not reverse and arr[j] < arr[min_idx]) or (reverse and arr[j] > arr[min_idx]):
                min_idx = j
        
        # Insert instead of swapping to make it stable
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key

arr = [10, 9, 8, 7, 6, 5]
selection_sort_unstable(arr)
print(arr)
selection_sort_unstable(arr, reverse = True)
print(arr)

arr = [10, 9, 8, 7, 6, 5]
selection_sort_stable(arr)
print(arr)
selection_sort_stable(arr, reverse = True)
print(arr) 