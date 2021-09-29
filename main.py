import random
import time

def ineffective_search(lists, objetive):
    for i in range(len(lists)):
        if lists[i] == objetive:
            return i
    return -1

def binary_search(lists, objetive, limit_min = None, limit_max = None):
   
    # Interval limit of the list
    if limit_min is None:
       limit_min = 0 # Start of the list
    if limit_max is None:
        limit_max = len(lists)-1 # End of the list
    # End intervals

    if limit_max < limit_min:
        return -1

    middle_point = (limit_min + limit_max) // 2 # middle point of the data in the list

    if lists[middle_point] == objetive:
        return middle_point

    elif objetive < lists[middle_point]:
        return binary_search(lists, objetive, limit_min, middle_point-1)
    else:
        return binary_search(lists, objetive, middle_point+1, limit_max)

if __name__ == '__main__':

    size = 1000
    initial_conjuct = set()

    while len(initial_conjuct) < size:
        initial_conjuct.add(random.randint(-3 * size, 3 * size))

    ordene_list= sorted(list(initial_conjuct)) 

    # ineffective_search
    start = time.time()
    for objetive in ordene_list:
        ineffective_search(ordene_list, objetive)
    end = time.time()

    print(f"ineffective search time: {end - start}s")

    # Binary search
    start = time.time()
    for objetive in ordene_list:
        ineffective_search(ordene_list, objetive)
    end = time.time()

    print(f"Binary search time: {end - start}s")
