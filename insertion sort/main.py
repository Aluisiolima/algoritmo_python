# ==============================
#     Test Insertion Sort 
#      Organize an array
# ==============================
# What is Insertion Sort?
# Insertion sort is an algorithm that sorts a list in a method to check if the next item is greater or lesser. sorting the list one by one being your worst case Θ(n²).

array : list[int] = [1,4,53,60,2,7,4,7]

def insertion_sort_increasing(array : list[int]) -> list[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Move elements of array[0..i-1], that are greater than key,
        # one position ahead of their current position
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key  # Insert key at the correct position

    return array 


print(f"{insertion_sort_increasing(array=array)}")

def insertion_sort_decreasing(array : list[int]) -> list[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Move elements of array[0..i-1], that are greater than key,
        # one position ahead of their current position
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key  # Insert key at the correct position

    return array 

print(f"{insertion_sort_decreasing(array=array)}")