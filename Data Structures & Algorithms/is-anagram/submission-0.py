class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        boing = {}
        bao = {}

        for x in s:
            if x not in boing:
                boing[x] = 1
            else:
                boing[x] += 1
        
        for x in t:
            if x not in bao:
                bao[x] = 1
            else:
                bao[x] += 1
        return bao == boing
        