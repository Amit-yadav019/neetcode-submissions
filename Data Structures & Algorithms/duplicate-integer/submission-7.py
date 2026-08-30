class Solution:
    def hasDuplicate(self,arr:list[int]) -> bool:
        n = len(arr)
        seen = set()
        for i in arr:
            if i in seen :
                return True 
            seen.add(i)
        return False    


        

        

