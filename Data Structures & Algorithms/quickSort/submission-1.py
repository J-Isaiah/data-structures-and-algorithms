# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.start_sort(0, len(pairs)-1, pairs)
        return pairs

    def start_sort(self,start, end, list_section):
        if start >= end:
            return
        piviot = list_section[end].key
        point = start
        print('end of list piviot is: ', piviot)

        for i in range(start, end):
            if list_section[i].key < piviot:
                list_section[i], list_section[point] = list_section[point], list_section[i]
                point +=1

        list_section[point], list_section[end] = list_section[end], list_section[point]
        self.start_sort(start, point-1,list_section)
        self.start_sort(point+1,end, list_section)

        return list_section
        