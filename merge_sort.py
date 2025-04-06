# ==============================
#     Test Merge Sort 
#      Organize an array
# ==============================
# What is Merge Sort?
# Merge sort  is an algorithm like a divide and conquer method, 
# where the problem is divided into smaller problems until we reach
# the solution of the subproblems and we unite everything, 
# thus concluding the larger problem.
#  O(n log n)

def merge_sort(arr : list[int], left : int, right : int):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr : list[int], left : int, mid : int, right : int):
    i, j, k = left, mid + 1, 0
    temp = [0] * (right - left + 1)

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(temp)):
        arr[left + i] = temp[i]

# Exemplo de uso:
arr : list[int] = [32,457,42573,4,7,5,4,1,2,47,4747]
merge_sort(arr, 0, len(arr) - 1)

