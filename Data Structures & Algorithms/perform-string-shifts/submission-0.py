class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        bro = []

        for x in s:
            bro.append(x)

        for bruh in shift:
            if bruh[0] == 0:
                for x in range(bruh[1]):
                    bah = bro.pop(0)
                    bro.append(bah)
            elif bruh[0] == 1:
                for x in range(bruh[1]):
                    bah = bro.pop()
                    bro.insert(0, bah)
                print(bro)
        return "".join(bro)