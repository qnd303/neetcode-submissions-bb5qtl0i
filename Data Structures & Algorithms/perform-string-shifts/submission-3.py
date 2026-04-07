class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        
        for x in shift:
            if x[0] == 0:
                net -= x[1]
            if x[0] == 1:
                net += x[1]

        net %= len(s)

        return s[-net:] + s[:-net]