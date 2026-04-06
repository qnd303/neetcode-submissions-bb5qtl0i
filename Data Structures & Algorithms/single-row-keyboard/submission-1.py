class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        boom = {}
        result = 0

        for i, x in enumerate(keyboard):
            if x not in boom:
                boom[x] = i

        pre = boom[keyboard[0]]

        for x in word:
            result += abs(boom[x] - pre)
            pre = boom[x]
        return result