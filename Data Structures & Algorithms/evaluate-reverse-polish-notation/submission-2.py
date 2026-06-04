class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator =['+','-','/','*']
        stack=[]
        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            if i in operator:
                temp_2=stack.pop()
                temp_1=stack.pop()
                
                if i== '+':
                    temp=temp_1+temp_2
                    stack.append(temp)
                elif i== '-':
                    temp= temp_1-temp_2
                    stack.append(temp)
                elif i== '*':
                    temp =int(temp_1)*int(temp_2)
                    stack.append(temp)
                else:
                    temp=int(temp_1/temp_2)
                    stack.append(temp)
        return int(stack.pop())