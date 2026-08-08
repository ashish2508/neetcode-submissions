class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count = Counter(nums)
        ans = set()

        for x in combinations(nums, 3):
            for num in x:
                count[num] -= 1

            needed = target - sum(x)

            if count[needed] > 0:
                ans.add(tuple(sorted((*x, needed))))

            for num in x:
                count[num] += 1

        return [list(x) for x in ans]