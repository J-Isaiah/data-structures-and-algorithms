class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        window = blocks[i:k]

        total = window.count("W")
        i += 1
        cur_count = total
        while i+k <= len(blocks):
            left = blocks[i-1]
            right = blocks[i+k-1]
            
            if left == "W":
                cur_count -=1
            if right == "W":
                cur_count+=1

            total = min(cur_count, total)
            i +=1
            

            
        return total




            

        
            
        