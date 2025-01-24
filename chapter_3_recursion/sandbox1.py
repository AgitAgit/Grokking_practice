
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