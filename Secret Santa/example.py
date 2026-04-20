import random

my_list = ["apple", "banana", "cherry", "cranberry", "blueberry", "strewberry", "peach"]
for i in range(1, len(my_list)+1):
    item = random.choice(my_list)
    print(item)
    my_list.remove(item)
