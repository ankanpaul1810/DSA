class Solution:
  def longestSubsequence(self, s: str, k: int) -> int:
    length = 0
    current_value = 0
    n = len(s)

    for i in range(n - 1, -1, -1):
      char = s[i]
      
      if char == '0':
        length += 1
      else:
        if length >= 31:
          continue
          
        power_of_2 = 1 << length
        
        if current_value + power_of_2 <= k:
          current_value += power_of_2
          length += 1
          
    return length