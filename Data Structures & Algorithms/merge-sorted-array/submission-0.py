class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        r = []
        i = 0
        j = 0

        while i < m and j < n:
            if a[i] < b[j]:
                r.append(a[i])
                i += 1
            else:
                r.append(b[j])
                j += 1

        r.extend(a[i:m])
        r.extend(b[j:n])

        for i in range(m + n):
            a[i] = r[i]





            