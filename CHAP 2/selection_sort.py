# Time Complexity: O(n^2) (Always)

# Space Complexity: O(1) (Always)

# We can make the time complexity in best case to O(n)
# By coding a checker if the array is already sorted or not in every iteration
# But it will increase the time needed for every iteration

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

def selection_sort_stable_sorted_checker(arr, reverse = False):
    size = len(arr)
    
    for i in range(size - 1):
        # Checking for the best case
        flag = True
        for k in range(i, size - 1):
            if (not reverse and arr[k] > arr[k + 1]) or (reverse and arr[k] < arr[k + 1]):
                flag = False
                break
        
        if flag:
            break
        
        min_idx = i
        for j in range(i+1, size):
            if (not reverse and arr[j] < arr[min_idx]) or (reverse and arr[j] > arr[min_idx]):
                # It does not print means that the checker is working
                print("checked")
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

arr = [5, 6, 7, 8, 9, 10]
selection_sort_stable_sorted_checker(arr)
print(arr)
arr = [10, 9, 8, 7, 6, 5]
selection_sort_stable_sorted_checker(arr, reverse = True)
print(arr) 