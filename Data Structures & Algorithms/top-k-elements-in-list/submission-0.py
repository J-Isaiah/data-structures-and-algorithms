class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = {}
        result = []

        for n in nums:
            if n  not in b:
                b[n] = 1
                continue
            b[n] += 1

            
            
            
            

        for i in range(k):
            max_key = max(b, key=b.get)
            result.append(max_key)
            b.pop(max_key)

        return result







        