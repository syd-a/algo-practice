def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    result = merge(merge_sort(left), merge_sort(right))
    return result

def merge(sorted_left, sorted_right):
    result = []
    i = 0
    j = 0
    while (i < len(sorted_left)) and (j < len(sorted_right)):
        if sorted_left[i] <= sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    result.extend(sorted_left[i:])
    result.extend(sorted_right[j:])
    return result

def use_merge_sort():
    arr = [7, 5, 17, 9, 31, 22]
    print("unsorted array: ", arr)
    print("sorted array: ", merge_sort(arr))

if __name__ == '__main__':
    use_merge_sort()
