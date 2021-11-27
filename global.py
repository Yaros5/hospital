def binary_search(ser, item):
    global guess, mid
    low = 0
    hig = len(ser) - 1
    while low <= hig:
        mid = (low + hig) // 2
        guess = ser[mid]
        if guess == item:
            return mid
        if guess > item:
            hig = mid - 1
        else:
            low = mid + 1
    return None
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))
dict = {
}