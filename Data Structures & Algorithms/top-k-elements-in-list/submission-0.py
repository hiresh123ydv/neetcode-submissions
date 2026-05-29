class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in range(0,len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        sorted_hashmap=sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        result=[]
        count=0
        for num in sorted_hashmap:
            result.append(num[0])
            count+=1
            if count==k:
                return result




        




        