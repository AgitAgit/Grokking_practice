#4.1
numbers_1 = [1,1,7,9]
def sum(arr):
    if(len(arr) == 0):
        print("0")
        return 0
    print(f"{arr[0]} + ")
    return arr[0] + sum(arr[1:])

# print("=",sum(numbers_1))

#4.2
def listLen(list):
    if(list == []):
        return 0
    return 1 + listLen(list[1:])

list1 = []
list2 = [3]
list3 = [5, 6, 7]
list4 = [-1, -3000, 0.2, 7, -1]

# print(sum(list1))
# print(sum(list2))
# print(sum(list3))
# print(sum(list4))

# print(listLen(list1))
# print(listLen(list2))
# print(listLen(list3))
# print(listLen(list4))

#4.3
def maxNum(list, max):
    if(list == []): return max
    if(list[0] > max): return maxNum(list[1:], list[0])
    return maxNum(list[1:], max)

# print(maxNum(list1, 0))
# print(maxNum(list2, 0))
# print(maxNum(list3, 0))
# print(maxNum(list4, 0))

# 4.4
# the base case for binary search is when either the number has been found or the index of the larger
# pointer is smaller or equal to the smaller pointer.
# the recursive case is to call the binary search function either with smaller or larger
# pointers increased or decreased to pass over the middle pointer

# 4.5
# o(n)

# 4.6
# o(n)

# 4.7
# o(1)

# 4.8
# o(n^2)