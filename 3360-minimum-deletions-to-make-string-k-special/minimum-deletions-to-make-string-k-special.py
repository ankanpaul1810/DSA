from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        min_deletions = float('inf')

        # Try to keep every frequency between [f, f + k] for each f in freq
        for i in range(n):
            base = freq[i]
            deletions = 0
            # delete chars with freq < base
            deletions += sum(freq[:i])
            # delete part of chars with freq > base + k
            for j in range(i + 1, n):
                if freq[j] > base + k:
                    deletions += freq[j] - (base + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
