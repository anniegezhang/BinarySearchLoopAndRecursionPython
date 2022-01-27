# while loop
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [1, 2, 3, 4]
target = 2
print(binarySearch(arr, target))

arr = [1, 3, 4, 5]
target = 2
print(binarySearch(arr, target))

# recursive

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr[left: mid], target)
        else:
            return binarySearch(arr[mid + 1: right], target)
    return -1
    


arr = [1, 2, 3, 4]
target = 2
print(binarySearch(arr, target))

arr = [1, 3, 4, 5]
target = 2
print(binarySearch(arr, target))