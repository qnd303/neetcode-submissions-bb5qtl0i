class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        one = 0
        two = 0

        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        while two < len(t) and one < len(s):
            if s[one] == t[two]:
                one += 1
                two += 1
            else:
                two += 1
        return one == len(s)