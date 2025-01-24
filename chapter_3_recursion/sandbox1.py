
def countdown(counter):
    print(counter)
    if(counter == 1):
        return
    countdown(counter - 1)

# countdown(5)