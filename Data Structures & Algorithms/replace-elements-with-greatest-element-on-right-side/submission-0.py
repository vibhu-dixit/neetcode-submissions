class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)-1
        maxx=-1
        for i in range(n,-1,-1):
            curr=arr[i]
            arr[i]=maxx
            maxx=max(curr,arr[i])
            
        return arr