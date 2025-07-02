import collections

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        # Step 1: Preprocessing - Group characters and count lengths
        counts = collections.Counter()
        if not word:
            return 0
        
        m = 0
        total_ways = 1
        current_len = 0
        for i in range(len(word)):
            current_len += 1
            if i + 1 == len(word) or word[i] != word[i+1]:
                counts[current_len] += 1
                total_ways = (total_ways * current_len) % MOD
                m += 1
                current_len = 0

        if m >= k:
            return total_ways
        
        # Step 2: Calculate ways for sum of lengths < k
        n = k - m
        if n <= 0:
            return total_ways

        # Precompute modular inverses up to n
        inv = [0] * (n + 1)
        if n > 0:
            inv[1] = 1
        for i in range(2, n):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

        # --- Polynomial Logarithm ---
        log_final_poly = [0] * n
        for L, c in counts.items():
            if L > 1:
                # log(1+...+x^{L-1}) = log(1-x^L) - log(1-x)
                for j in range(1, n):
                    term = inv[j]
                    if j % L == 0:
                        term = (term - inv[j // L] + MOD) % MOD
                    log_final_poly[j] = (log_final_poly[j] + c * term) % MOD
        
        # --- Polynomial Exponentiation ---
        # P(x) = exp(log_final_poly) mod x^n
        # Using formula: i*P_i = sum_{j=1..i} j*A_j*P_{i-j}
        P = [0] * n
        P[0] = 1
        for i in range(1, n):
            val = 0
            for j in range(1, i + 1):
                term = (j * log_final_poly[j]) % MOD
                term = (term * P[i - j]) % MOD
                val = (val + term) % MOD
            P[i] = (val * inv[i]) % MOD
            
        ways_less_than_k = sum(P) % MOD
        
        # Step 3: Final result
        return (total_ways - ways_less_than_k + MOD) % MOD