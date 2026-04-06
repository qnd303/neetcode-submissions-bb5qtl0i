class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        bro = -1
        bruh = {}
        result = -1
        for i, x in enumerate(nums):
            if x not in bruh:
                bruh[x] = 1
            else:
                bruh[x] += 1
        for x in bruh:
            if bruh[x] == 1:
                result = max(x, result)
        return result