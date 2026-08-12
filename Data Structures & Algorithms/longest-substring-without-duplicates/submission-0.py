class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        ans = ""

        for i in s:
            if i in res:
                res = res[res.index(i) + 1:]

            res += i

            if len(res) > len(ans):
                ans = res

        return len(ans)