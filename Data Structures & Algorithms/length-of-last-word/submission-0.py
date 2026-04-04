class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        brah = s.rstrip()
        grah = brah.split(" ")
        boi = str(grah[-1])
        return len(boi)
