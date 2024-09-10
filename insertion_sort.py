# Insertion Sort
def insertion_sort(array):
    n = len(array)
    i = 1
    while i < n:
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = current
        i = i + 1

    return array


data = [9, 5, 1, 4, 3]
name = ["shiv", "sasha", "lisa", "barry"]
print(insertion_sort(name))
