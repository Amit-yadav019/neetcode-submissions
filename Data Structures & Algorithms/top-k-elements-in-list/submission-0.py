class Solution:

  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    # 1. Count frequencies using a plain dictionary
    freq_map = {}
    for num in nums:
      freq_map[num] = freq_map.get(num, 0) + 1

    # 2. Bucket array where index represents frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]

    for num, count in freq_map.items():
      buckets[count].append(num)

    # 3. Gather the top k elements from highest frequency to 1
    result = []
    for freq in range(n, 0, -1):
      for num in buckets[freq]:  # Line 18
        result.append(num)  # Line 19: indented under the inner for loop
        if len(result) == k:
          return result

    return result
  