def binary_search(lst, target):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1   
    return -1        