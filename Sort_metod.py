## Сортировка пузырьком
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        all_sorted = True
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]
            all_sorted = False
            arr[j+1], arr[j] = arr[j], arr[j+1]
        if all_sorted:
            return arr
##========================================================
## Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
##========================================================
## Сортировка вставками
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr
##========================================================
## Сортировка слиянием
def merge_sort(arr):
    ## Возвращаем массив из одного элемента
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr)

def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor+right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor+right_cursor] = left[left_cursor]
    
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor+right_cursor] = right[right_cursor]
    return merged
##========================================================
## Быстрая сортировка
def quick_sort(array, start, stop):
    if start >= stop: return
    left = start
    right = stop
    x = array[(left + right) // 2]
    while left <= right:
        while array[left] < x: left += 1
        while array[right] > x: right -= 1
    if left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    quick_sort(array, start, right)
    quick_sort(array, left, stop)