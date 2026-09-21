class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimal soln. 
        # usnig set data structure 
        n = len(nums)
        if len(nums) == 0 :
            return 0 
        nums_set = set(nums)
        longest = 1 
        for num in nums_set :
            if num - 1 not in nums_set :
                count = 1
                x = num 
                while x + 1 in nums_set :
                    x = x + 1
                    count = count + 1
                longest = max(longest,count)
        return longest             




        
        