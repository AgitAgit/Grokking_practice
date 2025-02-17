from os import listdir
from os.path import isfile, join
from collections import deque

directory_tree = {}
directory_tree["PICS"] = ["2001", "odyssey.png"]
directory_tree["2001"] = ["a.png", "space.png"]

# directory_tree_2 = {
#     "PICS":[
#         {"2001":["a.png", "space.png"]},
#         "odyssey.png"
#         ]
# }

# my code
def breadth_first_print(tree, root_name):
    print_queue = deque() 
    print_queue += [f"{root_name}"]
    while print_queue:
        if(print_queue[0] in tree):
            print_queue += tree[print_queue[0]]
        print(print_queue.popleft())
    
# breadth_first_print(directory_tree, "PICS")

# from the book:
def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)

# printnames("pics")

# Can I do this without a for loop?
def my_rec_printnames(path, name):
    fullpath = join(path,name)
    if isfile(fullpath):
        print(name)
        return
    dir = listdir(fullpath)
    for element in dir:
        my_rec_printnames(fullpath, element)

# my_rec_printnames("","pics")


# suppose I have a tree and I want a list of the it's leaves?
def my_rec_printnames2(path, name):
    fullpath = join(path,name)
    if isfile(fullpath):
        print(name)
        return name
    dir = listdir(fullpath)


