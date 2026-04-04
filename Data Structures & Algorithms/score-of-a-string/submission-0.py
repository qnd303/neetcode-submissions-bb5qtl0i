class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0
        total = 0
        while left < len(s) - 1:
            total += abs(ord(s[left]) - ord(s[left+1]))
            left += 1
        return total