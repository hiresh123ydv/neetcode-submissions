class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        for i in range(0,n):
            prod=1
            for j in range(0,n):
                if j!=i:
                    prod*=nums[j]
                else:
                    continue    
            result.append(prod)
        return result           


        
        