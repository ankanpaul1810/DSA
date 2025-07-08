import bisect
from typing import List

class Solution:
  def maxValue(self, events: List[List[int]], k: int) -> int:
    """
    Calculates the maximum sum of values by attending at most k events using
    a top-down dynamic programming approach with memoization.
    """
    n = len(events)
    
    # Sort events by their start day to process them in chronological order.
    events.sort()
    
    # Memoization table: memo[i][k_left] stores the max value for the subproblem
    # starting at event `i` with `k_left` attendance slots remaining.
    # Initialized to -1 to mark states as not yet computed.
    memo = [[-1] * (k + 1) for _ in range(n)]

    # Pre-calculate start days for efficient binary search.
    start_days = [event[0] for event in events]

    def dfs(i: int, k_left: int) -> int:
        """
        Calculates the maximum value obtainable from events[i:] with k_left slots.
        """
        # Base case: No more slots left or no more events to consider.
        if k_left == 0 or i >= n:
            return 0

        # If this subproblem has been solved, return the stored result.
        if memo[i][k_left] != -1:
            return memo[i][k_left]

        # --- Decision for event `i` ---

        # Option 1: Skip event `i`.
        # Move to the next event `i+1` with the same number of slots `k_left`.
        res_skip = dfs(i + 1, k_left)

        # Option 2: Attend event `i`.
        # Find the index of the next event that starts after event `i` ends.
        # `bisect_right` finds the insertion point for `events[i][1]`, which
        # corresponds to the index of the first event starting > `events[i][1]`.
        end_day = events[i][1]
        next_i = bisect.bisect_right(start_days, end_day)
        
        # The total value is the current event's value plus the max value from
        # the subsequent non-overlapping events, using one less slot.
        res_attend = events[i][2] + dfs(next_i, k_left - 1)

        # Store the best result for the current state (i, k_left) and return it.
        memo[i][k_left] = max(res_skip, res_attend)
        return memo[i][k_left]

    # Start the recursion from the first event (index 0) with `k` slots available.
    return dfs(0, k)