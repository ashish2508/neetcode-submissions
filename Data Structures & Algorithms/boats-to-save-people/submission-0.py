class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort()

        left = 0
        right = len(p) - 1
        cnt = 0

        while left <= right:
            if p[left] + p[right] <= l:
                left += 1

            right -= 1
            cnt += 1

        return cnt