class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        k=len(s1)
        for r in range(len(s2)):
            window[s2[r]] += 1

            if r >= k:
                window[s2[r-k]] -= 1
                if window[s2[r-k]] == 0:
                    del window[s2[r-k]]

            if window == need:
                return True

        return False
 