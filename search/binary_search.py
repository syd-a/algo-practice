import random

def bin_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bin_search(arr, target, left, mid - 1)
    elif arr[mid] < target:
        return bin_search(arr, target, mid + 1, right)

def use_bin_search():
    arr = [2, 3, 7, 11, 13, 17, 19, 23]
    searches = [(arr[i], i) for i in range(len(arr))]
    random.shuffle(searches)
    for search_val, search_ind in searches:
        ret_ind = bin_search(arr, search_val, 0, len(arr) - 1)
        is_success = "Success" if ret_ind == search_ind else "ERROR"
        print(f"{is_success}: searched for {search_val}, expected index {search_ind}, received index {ret_ind};")

if __name__ == "__main__":
    use_bin_search()
