class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj={}
        li=[]
        for i in nums:
            maj[i]=maj.get(i,0)+1
        for key in maj:
            if maj[key]>len(nums)//3:
                li.append(key)
        return li
            
            