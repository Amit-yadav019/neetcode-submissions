class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict = {}
        for i in range(n):
            need = target - nums[i]
            if need in dict:
                return [dict[need],i]
            dict[nums[i]] = i

        return []        
