# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs)

    def mergeSortHelper(self,l):
        if len(l)<=   1:
            return l

        full = len(l)
        half = full//2


        front_half = self.mergeSortHelper(l[0:half])
        back_half = self.mergeSortHelper(l[half:])

        return self.merge(front_half, back_half)

    def merge(self,front_half, back_half):
        full_list = []
        back = 0
        front = 0

        while front< len(front_half) and back<len(back_half):
            if front_half[front].key <= back_half[back].key:
                full_list.append(front_half[front])
                front+=1
                continue
            else:
                full_list.append(back_half[back])
                back+=1
                continue
        full_list.extend(front_half[front:])
        full_list.extend(back_half[back:])
     
        return full_list


