class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kthCount = Counter(nums).most_common(k)
        answer = []
        for key, value in kthCount:
            answer.append(key)
        return answer
        