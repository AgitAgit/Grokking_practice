
def countdown(counter):
    print(counter)
    if(counter == 1):
        return
    countdown(counter - 1)

# countdown(5)

def factorial(num):
    if(num == 0):
        return 1
    return num * factorial(num - 1)

# result = factorial(4)
# print(result)

def sum(list):
    if(len(list) == 0): 
        return 0
    return list[0] + sum(list[1:])

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

def maxNum(list, max):
    if(list == []): return max
    if(list[0] > max): return maxNum(list[1:], list[0])
    return maxNum(list[1:], max)

# print(maxNum(list1, 0))
# print(maxNum(list2, 0))
# print(maxNum(list3, 0))
# print(maxNum(list4, 0))

