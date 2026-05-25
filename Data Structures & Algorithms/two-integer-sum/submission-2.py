class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            d[nums[i]]=i
        for i in range(0,len(nums)):
            x=target-nums[i]   
            if x in d and d[x]!=i:
                return [i,d[x]]


        