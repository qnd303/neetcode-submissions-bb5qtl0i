class Solution:
    def confusingNumber(self, n: int) -> bool:
        j = "23457"
        k = str(n)

        for i in range(len(j)):
            if j[i] in k:
                return False
        w = set(k)
        if len(w) == 1:
            if '1' in k:
                return False
            if '0' in k:
                return False
            if '8' in k:
                return False
        return True