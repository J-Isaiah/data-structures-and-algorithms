class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        total = float('inf')

        while i + k <= len(blocks):
            window = blocks[i:i + k]

            total = min(window.count("W"), total)

            i += 1
        return total




            

        
            
        