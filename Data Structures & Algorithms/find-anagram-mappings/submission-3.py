class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        yo = {}
        result = []
        for i, num in enumerate(nums2):
            yo[num] = i

        for x in nums1:
            result.append(yo[x])
        return result