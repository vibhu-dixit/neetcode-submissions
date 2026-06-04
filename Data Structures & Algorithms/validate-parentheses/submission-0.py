class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        paranth = [']', '}', ')']
        stack = []
        for c in s:
            if c not in paranth:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if temp != pairs[c]:
                        return False
        return len(stack) == 0