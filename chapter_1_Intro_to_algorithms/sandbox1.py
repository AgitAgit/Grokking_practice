def binary_search(arr, item):
    low = 0
    high = len(arr) -1
    while(low <= high):
        mid = (low + high) // 2
        print(mid)
        if(arr[mid] == item):
            return mid
        if(arr[mid] < item):
            low = mid + 1
        if(item < arr[mid]):
            high = mid - 1
    return None

arr1 = [0, 1, 2, 3]
arr2 = []
for i in range(100):
    arr2.append(i)
result = binary_search(arr2, 3)
print("index found: ",result)
if(result):
    print(result)
else:
    print("not found")