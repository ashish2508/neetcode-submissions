class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        mxc = 0

        for num in num_set:
            if num - 1 not in num_set:
                cnt = 1

                while num + cnt in num_set:
                    cnt += 1

                mxc = max(mxc, cnt)

        return mxc