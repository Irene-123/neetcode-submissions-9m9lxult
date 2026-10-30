class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1221
        # 122
        # 12 + 2
        # rev = 2*10 + 2 = 22 
        # 1 + 2 rev = 22*10 + 1 

        if x < 0:
            return False
        num = x
        rev = 0

        while num:
            digit = num%10
            num //= 10 

            rev = rev*10 + digit

        return rev == x


            
        

