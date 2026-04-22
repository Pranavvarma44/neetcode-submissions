class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=nums.copy()
        nums.extend(nums2)
        return nums
        