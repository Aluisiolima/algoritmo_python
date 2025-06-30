# This code implements a binary search algorithm to find the index of a target element in a sorted array.
# Binary Search Algorithm
# The binary search algorithm works by repeatedly dividing the search interval in half.
# If the value of the search key is less than the item in the middle of the interval

def search_bin(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


arr = range(1, 257)
target = 256
result = search_bin(arr, target)
if result is not None:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")