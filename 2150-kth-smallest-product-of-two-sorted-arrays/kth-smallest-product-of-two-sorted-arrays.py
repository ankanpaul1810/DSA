import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        low, high = -10**10, 10**10
        
        def count_pairs(mid):
            cnt = 0
            for x in nums1:
                if x == 0:
                    if mid >= 0:
                        cnt += len(nums2)
                elif x > 0:
                    t = mid // x
                    idx = bisect.bisect_right(nums2, t)
                    cnt += idx
                else:
                    t = mid // x
                    if mid % x != 0:
                        t += 1
                    idx = bisect.bisect_left(nums2, t)
                    cnt += len(nums2) - idx
            return cnt
        
        while low < high:
            mid_val = (low + high) // 2
            if count_pairs(mid_val) >= k:
                high = mid_val
            else:
                low = mid_val + 1
        return low