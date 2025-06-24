from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, val in enumerate(nums) if val == key]
        result = set()

        for j in key_indices:
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                result.add(i)
        return sorted(result)