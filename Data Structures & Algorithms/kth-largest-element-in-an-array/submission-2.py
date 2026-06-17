class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-n for n in nums]
        heapq.heapify(nums)
        ans = None
        for _ in range(k):
            ans = -heapq.heappop(nums)
        return ans