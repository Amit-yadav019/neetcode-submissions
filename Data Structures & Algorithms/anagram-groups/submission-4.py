class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs :
            key = "".join(sorted(word))
            # print(key)
            if key not in d :
                d[key] = []
            d[key].append(word)   
            # print(d)

        return list(d.values())     