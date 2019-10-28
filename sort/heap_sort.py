class Heap:
    def __init__(self, n):
        self.size = 0
        self.data = [None for i in range(10)]

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
        if self.is_empty:
            raise Exception("Heap is empty.")

        result = self.data[0]

        self.data[0] = self.data[size - 1]
        self.data[size - 1] = None
        self.size -= 1
        i = 0
        moreToSwitch = true
        while (moreToSwitch):
            smallest_ind = i
            smallest_val = self.data[i]

            left_ind = i * 2
            right_ind = i * 2 + 1

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
                moreToSwitch = false
            else:
                self.data[i], self.data[smallest_ind] = self.data[smallest_ind], self.data[i]
                i = smallest_ind

        return result
