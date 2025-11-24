#linear search algorithm
#checks elements in a list sequwntially until the desired element is found

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#use when the array is small or uhsorted 
#time complexity: O(n)
#space complexity: O(1)

 