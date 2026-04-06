class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bruh = {}
        count = 0
        
        for x in s:
            if x not in bruh:
                bruh[x] = 1
            else:
                bruh[x] += 1

        for x in bruh:
            if bruh[x] % 2 == 1:
                count += 1

        if count > 1:
            return False
        return count < 2
