import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k

        heapq.heapify(self.h)
        while self.k < len(nums):
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        self.h.append(val)
        heapq.heapify(self.h)
        while self.k < len(self.h):
            heapq.heappop(self.h)

        return self.h[0]
