def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(arr, left , right)

def merge(arr, left, right):
    i = j = k = 0
    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [5, 3, 8, 1, 2]
print("Original Array:", arr)

merge_sort(arr)

print("Sorted Array:", arr)
