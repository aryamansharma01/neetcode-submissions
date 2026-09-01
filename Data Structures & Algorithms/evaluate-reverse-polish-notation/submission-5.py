class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i=="+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif i=="-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif i=="*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif i=="/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack.pop()

                
