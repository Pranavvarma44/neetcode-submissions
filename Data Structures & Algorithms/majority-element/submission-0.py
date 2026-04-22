class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for num in nums:
            s[num]=s.get(num,0)+1
            if s[num]>len(nums)//2:
                return num