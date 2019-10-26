import random

def quick_sort(array):
    if len(array) <= 1:
        return array

    arr = array[:]
    random.shuffle(arr)

    pivot = arr.pop()
    higher = []
    lower = []
    for ele in arr:
        if ele >= pivot:
            higher.append(ele)
        else:
            lower.append(ele)
    result = lower + [pivot] + higher
