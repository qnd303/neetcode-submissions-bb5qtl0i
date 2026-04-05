class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        yo = []
        for i in nums1:
            count = 0
            for j in range(len(nums1)):
                if i == nums2[j] and count == 0:
                    yo.append(j)
                    count += 1

        return yo