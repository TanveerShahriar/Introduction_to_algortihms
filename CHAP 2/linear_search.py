# Time Complexity:

# Best  Case : O(1)
# Avg   Case : O(n)
# Worst Case : O(n)

# Space Complexity: O(1) (Always)

def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i 
    
    return -1

arr = [4, 7, 2, 9, 1, 5]
print(linear_search(arr, 5))
print(linear_search(arr, 6))