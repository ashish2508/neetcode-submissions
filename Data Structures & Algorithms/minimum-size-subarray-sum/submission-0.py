class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        left = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if ans == len(nums) + 1 else ans