class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        h = {}

        for email in emails:
            domain = email.split('@')[-1]
            front = email.split("+")[0]
            front = front.replace('.','')

            if not front+"@"+domain in h:
                h[front+"@"+domain] = email
                res += 1

        return res

            





            
            
        
        