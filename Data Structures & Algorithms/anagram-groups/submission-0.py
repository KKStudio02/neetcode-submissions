class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        anagramsGroup = {} #dict
        for tempstrs in strs:
            key = "".join(sorted(tempstrs))
            if(key in anagramsGroup):
                anagramsGroup[key].append(tempstrs)
            else:
                anagramsGroup.setdefault(key, []).append(tempstrs)
        result = []
        for value in anagramsGroup.values():
            result.append(value)
        return result
            

            
        