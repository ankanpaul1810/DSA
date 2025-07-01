class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        count = 0
        i = 0

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            group_length = j - i
            if group_length > 1:
                count += group_length - 1
            i = j

        return count + 1  