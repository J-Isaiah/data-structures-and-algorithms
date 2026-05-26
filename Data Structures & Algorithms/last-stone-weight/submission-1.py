import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            elif x < y:
                stone = y - x
                heapq.heappush(heap, -stone)
            elif x > y:
                stone = x - y
                heapq.heappush(heap, -stone)
        return -heap[0] if heap else 0
