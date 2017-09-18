def binary_search(List, item):
    low = 0
    high = len(List) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = List[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    
    print binary_search(my_list, 3)
    print binary_search(my_list, -1)