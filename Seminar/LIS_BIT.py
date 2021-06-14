def coordinateCompression(arr, n):
    s = dict()
    for i in range(n):
        s[arr[i]] = 1
 
    index = 0
    mp = dict()
 
    for itr in sorted(s):
        index += 1
        mp[itr] = index
    for i in range(n):
        arr[i] = mp[arr[i]]
 
def query(BIT, index, n):
    ans = 0
    while (index > 0):
        ans = max(ans, BIT[index])
         
        # Go to parent node
        index -= index & (-index)
    return ans
 
def update(BIT, index, n):
    x = query(BIT, index - 1, n)
    value = x + 1
    while (index <= n):
        BIT[index] = max(BIT[index], value)
        index += index & (-index)
 
def findLISLength(arr, n):
    coordinateCompression(arr, n)
    BIT = [0]*(n + 1)
 
    for i in range(n):
        update(BIT, arr[i], n)
 
    ans = query(BIT, n, n)
    return ans
 
arr=[6, 5, 1, 3, 2, 4, 8, 7]
n = len(arr)
ans = findLISLength(arr, n)
 
print(ans)