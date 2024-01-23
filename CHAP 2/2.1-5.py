# s   %2  //2
# ============
# 3    1    1
# 2    0    1
# 1    1    0
# 0    0    0

def add_binary_integers(arr1, arr2, n):
    res = [None] * (n + 1)
    
    carry = 0
    for i in range(n-1, -1, -1):
        s = arr1[i] + arr2[i] + carry
        carry = s // 2
        res[i + 1] = s % 2
    
    res[0] = carry
    
    return res 

a = [1, 1, 1, 1]
b = [1, 1, 1, 1]
print(add_binary_integers(a, b, len(a)))

a = [0, 1, 0, 0, 1, 0, 1, 0]
b = [0, 1, 1, 1, 0, 0, 0, 1]
print(add_binary_integers(a, b, len(a)))