class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        my_set=set()
        maxi=0
        for i in range(0,n):
            my_set.add(nums[i])
        c=0    
        for k in my_set:
            if k-1 not in my_set:   #start of seq
                c=1
                while k+c in my_set:
                    c+=1      
            maxi=max(maxi,c)   
        return maxi     


           
        


        