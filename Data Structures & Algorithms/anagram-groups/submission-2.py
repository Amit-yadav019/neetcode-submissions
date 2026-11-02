class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
   
      
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Array of 26 zeros, one for each lowercase English letter
            count = [0] * 26
            
            for char in s:
                # Find the index (0 for 'a', 1 for 'b', ..., 25 for 'z')
                count[ord(char) - ord('a')] += 1
                
            # Convert list to tuple so it can be hashed as a dictionary key
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())

