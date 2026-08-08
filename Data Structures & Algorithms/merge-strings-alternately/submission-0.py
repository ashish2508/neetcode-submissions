class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        s = []
        n = min(len(w1), len(w2))

        for i in range(n):
            s.append(w1[i])
            s.append(w2[i])

        if len(w1) > len(w2):
            s.extend(w1[n:])
        else:
            s.extend(w2[n:])

        return ''.join(s)