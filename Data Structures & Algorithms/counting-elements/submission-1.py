class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        boi = set(arr)
        for x in arr:
            if x + 1 in boi:
                count += 1
        return count