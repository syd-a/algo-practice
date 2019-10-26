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
    result = quick_sort(lower) + [pivot] + quick_sort(higher)
    return result

def use_quick_sort:
    arr = [7, 5, 17, 9, 31, 22]
    print("unsorted array: ", arr)
    print("sorted array: ", quick_sort(arr))

if __name__ == "__main__":
    use_quick_sort()
