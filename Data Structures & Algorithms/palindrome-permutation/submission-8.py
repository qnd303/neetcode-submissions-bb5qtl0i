class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bruh = {}
        count = 0
        allsame = set(s)

        if len(s) == 1:
            return True
        
        if len(allsame) == 1:
            return True
            
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

        for x in bruh:
            if bruh[x] % 2 == 0 and count == 0:
                return True
            if bruh[x] % 2 == 0 and count == 1:
                return True
        return False

