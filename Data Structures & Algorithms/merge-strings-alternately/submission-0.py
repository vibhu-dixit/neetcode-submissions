class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        n=len(w1)
        m=len(w2)
        res=[]

        for i in range(max(m, n)):
            if i < n:
                res.append(w1[i])
            if i < m:
                res.append(w2[i])
        return "".join(res)