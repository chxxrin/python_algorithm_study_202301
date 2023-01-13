arr = []
for i in range(9): 
    arr.append(int(input()))
all = sum(arr)

first = 0
second = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if all - arr[i] - arr[j] == 100:
            first = arr[i]
            second = arr[j]
arr.remove(first)
arr.remove(second)
arr.sort()
for i in arr:
    print(i)
