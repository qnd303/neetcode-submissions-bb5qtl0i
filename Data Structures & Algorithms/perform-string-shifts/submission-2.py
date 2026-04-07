class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        bro = []
        l = 0
        r = 0

        for x in s:
            bro.append(x)

        for bruh in shift:
            if bruh[0] == 0:
                l += bruh[1]
            if bruh[0] == 1:
                r += bruh[1]

        for x in range(l):
            bah = bro.pop(0)
            bro.append(bah)

        for x in range(r):
            bah = bro.pop()
            bro.insert(0, bah)
            
        return "".join(bro)