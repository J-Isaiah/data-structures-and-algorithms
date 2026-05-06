class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1]+=1
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i]>9 and i !=0:
                digits[i-1]+=1
                digits[i] = 0
            elif i == 0 and digits[i] > 9 :
                digits[i] = 0
                digits = [1] + digits


        return digits



            


    
    
    




        

        