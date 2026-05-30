class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod_0=1
        count=0
        for i in range(0,n):
            if nums[i]!=0:
                prod_0*=nums[i]
            else:
                count+=1    
        for i in range(0,n):
            if nums[i]==0 and count==1:
                nums[i]=prod_0
            elif nums[i]==0 and count>1:
                nums[i]=0
            elif nums[i]!=0 and count>=1:
                nums[i]=0
            else:
                nums[i]=int(prod_0/nums[i])  
        return nums          



              
        