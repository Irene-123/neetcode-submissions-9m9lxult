

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == "+":
                stack.append(stack.pop() + stack.pop())
            elif op == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif op == "*":
                stack.append(stack.pop()*stack.pop())
            elif op == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(op))
                
        
        return stack[-1]

        