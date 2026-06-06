class Solution:
    def isValid(self, s: str) -> bool:
        complete={'}':'{',']':'[',')':'('}
        paran=[']','}',')']
        stack=[]
        for p in s:
            if p not in paran:
                stack.append(p)
            else:
                if len(stack)==0:
                    return False
                else:
                    temp=stack.pop()
                    if temp!=complete[p]:
                        return False
        return len(stack)==0