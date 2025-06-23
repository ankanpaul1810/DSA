class Solution:
    def kMirror(self, k: int, n: int) -> int:        
        def to_base_k(num: int, base: int) -> str:
            if num == 0:
                return "0"
            res = ""
            while num > 0:
                res = str(num % base) + res
                num //= base
            return res

        count = 0
        total_sum = 0
        length = 1
        
        while count < n:
         
            half_len = (length + 1) // 2
            start_root_val = k**(half_len - 1)
            end_root_val = k**half_len
            
            for i in range(start_root_val, end_root_val):
                s_half = to_base_k(i, k)
              
                second_half = s_half[:length - half_len][::-1]
                s_palindrome_k = s_half + second_half
                
                num_base_10 = int(s_palindrome_k, k)
                
                if str(num_base_10) == str(num_base_10)[::-1]:
                    total_sum += num_base_10
                    count += 1
                    if count == n:
                        return total_sum
            
            length += 1
            
        return total_sum