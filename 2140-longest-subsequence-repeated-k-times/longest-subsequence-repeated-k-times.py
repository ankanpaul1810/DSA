def is_subsequence(s, pattern):
    if not pattern:
        return True
    i = 0
    for char in s:
        if i < len(pattern) and pattern[i] == char:
            i += 1
    return i == len(pattern)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        from collections import Counter
        freq_counter = Counter(s)
        candidate_chars = []
        max_freq = {}
        for char, count in freq_counter.items():
            if count >= k:
                candidate_chars.append(char)
                max_freq[char] = count // k
        candidate_chars.sort(reverse=True)
        max_len = min(n // k, 7)
        
        for L in range(max_len, 0, -1):
            def dfs(path):
                pattern = path * k
                if not is_subsequence(s, pattern):
                    return None
                if len(path) == L:
                    return path
                for c in candidate_chars:
                    if path.count(c) < max_freq[c]:
                        res = dfs(path + c)
                        if res is not None:
                            return res
                return None
            res = dfs("")
            if res:
                return res
        return ""