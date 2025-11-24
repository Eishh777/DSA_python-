#efficient in sorted array by repeatedly dividing the array into half

def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else: 
            high = mid + 1

    return -1

#use when array is sorted 
# time complexity O(log n)