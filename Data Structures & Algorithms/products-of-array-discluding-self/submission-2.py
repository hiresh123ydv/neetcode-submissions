class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        for i in range(0,n):
            if i==0:
                prefix[0]=1
            else:
                prefix[i]=prefix[i-1]*nums[i-1]    
        for j in range(n-1,-1,-1):
            if j==n-1:
                suffix[n-1]=1
            else:
                suffix[j]=nums[j+1]*suffix[j+1]
        result=[0]*n
        for x in range(0,n):
            result[x]=prefix[x]*suffix[x]     
        return result                   
        