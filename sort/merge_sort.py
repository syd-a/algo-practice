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
    while(len(sorted_left) > 0 and len(sorted_right) > 0):
        head_left = sorted_left[0]
        head_right = sorted_right[0]
        if head_left <= head_right:
            result.append(head_left)
            sorted_left = sorted_left[1:]
        else:
            result.append(head_right)
            sorted_right = sorted_right[1:]
    result.extend(sorted_left)
    result.extend(sorted_right)
    return result

if __name__ == '__main__':
    arr = [7, 5, 17, 9, 31, 22]
    print(arr)
    print(merge_sort(arr))
