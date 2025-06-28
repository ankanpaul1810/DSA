from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its index
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        
        # Sort by value descending and take top k elements
        top_k = sorted(indexed_nums, key=lambda x: -x[0])[:k]
        
        # Sort the selected top k elements by their original index to maintain order
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[1])
        
        # Extract just the values for the final subsequence
        return [num for num, idx in top_k_sorted_by_index]
