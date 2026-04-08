class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop() 
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)

        while stack and stars:
            if stars.pop() < stack.pop():
                return False 

        return not stack


        

        