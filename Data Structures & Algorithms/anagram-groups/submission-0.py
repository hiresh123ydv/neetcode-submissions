from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        d=defaultdict(list)
        for word in strs:
            sorted_s="".join(sorted(word))
            d[sorted_s].append(word)
        return list(d.values())   
                



        

        