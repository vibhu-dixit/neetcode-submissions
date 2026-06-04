class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        l,r=0,n-1
        cnt=0
        while l <= r:
            if people[r] > limit or people[l] + people[r] > limit:
                cnt += 1
                r -= 1
                continue
            else:
                cnt += 1
                l += 1
                r -= 1
        return cnt