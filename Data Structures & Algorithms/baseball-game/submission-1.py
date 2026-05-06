class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cur = 0
        total = []
        while cur < len(operations):
            num = operations[cur]
            if num == "+":
                add_op = int(total[-1]) + int(total[-2])
                total.append(add_op)
            elif num == "D":
                total.append(total[-1]*2)
            elif num =="C":
                total.pop()
            else: 
                total.append(int(num))
            cur += 1 
        print(total)
        return sum(total)




        