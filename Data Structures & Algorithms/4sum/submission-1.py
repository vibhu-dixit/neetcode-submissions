class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        # 1. Build all pair sums
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((nums[i] + nums[j], i, j))

        # 2. Sort by pair sum
        pairs.sort(key=lambda x: x[0])

        res = set()
        L, R = 0, len(pairs) - 1

        # 3. Two-pointer search
        while L < R:
            s = pairs[L][0] + pairs[R][0]

            if s < target:
                L += 1
            elif s > target:
                R -= 1
            else:
                # sums match target
                sumL = pairs[L][0]
                sumR = pairs[R][0]

                # collect all pairs with sumL
                left_list = []
                while L < R and pairs[L][0] == sumL:
                    left_list.append(pairs[L])
                    L += 1

                # collect all pairs with sumR
                right_list = []
                while R >= L and pairs[R][0] == sumR:
                    right_list.append(pairs[R])
                    R -= 1

                # combine all left × right pairs
                for _, i1, j1 in left_list:
                    for _, i2, j2 in right_list:
                        # all 4 indices must be distinct
                        if len({i1, j1, i2, j2}) == 4:
                            quad = sorted([nums[i1], nums[j1], nums[i2], nums[j2]])
                            res.add(tuple(quad))

        return [list(q) for q in sorted(res)]
