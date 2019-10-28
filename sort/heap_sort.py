class Heap:
    def __init__(self, n):
        self.size = 0
        self.data = [None for i in range(n)]

    def insert(self, item):
        self.data[self.size] = item
        i = self.size
        self.size += 1

        while (i > 0) and (self.data[i // 2] > self.data[i]):
            self.data[i // 2], self.data[i] = self.data[i], self.data[i // 2]
            i = i // 2

    def is_empty(self):
        return (self.size == 0)

    def pop(self):
        if self.is_empty():
            raise Exception("Heap is empty.")

        result = self.data[0]

        self.data[0] = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        i = 0
        more_to_switch = True
        while (more_to_switch):
            smallest_ind = i
            smallest_val = self.data[i]

            left_ind = i * 2 + 1
            right_ind = i * 2 + 2

            if left_ind < self.size:
                left_child = self.data[left_ind]
                if left_child < smallest_val:
                    smallest_ind = left_ind
                    smallest_val = left_child

            if right_ind < self.size:
                right_child = self.data[right_ind]
                if right_child < smallest_val:
                    smallest_ind = right_ind
                    smallest_val - right_child

            if smallest_val == self.data[i]:
                more_to_switch = False
            else:
                self.data[i], self.data[smallest_ind] = self.data[smallest_ind], self.data[i]
                i = smallest_ind

        return result

def use_heap_sort():
    arr = [7, 5, 17, 9, 31, 22]
    print("unsorted array: ", arr)

    heap = Heap(len(arr))
    for ele in arr:
        heap.insert(ele)

    sorted_arr = []
    while not heap.is_empty():
        sorted_arr.append(heap.pop())
    print("sorted array: ", sorted_arr)

if __name__ == "__main__":
    use_heap_sort()
