class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for s in tokens:
            if s in "+-*/":
                if s =="+":
                    temp1=stack.pop()
                    temp2=stack.pop()
                    res= int(temp1+temp2)
                    stack.append(res)
                elif s=="-":
                    temp1=stack.pop()
                    temp2=stack.pop()
                    res= int(temp2-temp1)
                    stack.append(res)
                elif s=='*':
                    temp1=stack.pop()
                    temp2=stack.pop()
                    res= int(temp2*temp1)
                    stack.append(res)
                else:
                    temp1=stack.pop()
                    temp2=stack.pop()
                    res= int(temp2/temp1)
                    stack.append(res)
            else:
                stack.append(int(s))
        return stack[0]
