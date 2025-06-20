class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def calculate_max_objective_value(s_moves: str, k_changes: int, objective_type: str) -> int:
         
            current_objective_value = 0
            negative_contributions_count = 0
            max_objective_value_so_far = 0

            for char_move in s_moves:
                delta = 0
                is_negative_contribution = False

                if objective_type == 'xy': 
                    if char_move == 'N' or char_move == 'E':
                        delta = 1
                    else:  
                        delta = -1
                        is_negative_contribution = True
                elif objective_type == 'xmy':  
                    if char_move == 'S' or char_move == 'E':
                        delta = 1
                    else:  
                        delta = -1
                        is_negative_contribution = True
                elif objective_type == 'mxy': 
                    if char_move == 'N' or char_move == 'W':
                        delta = 1
                    else: 
                        delta = -1
                        is_negative_contribution = True
                elif objective_type == 'mxmy':  
                    if char_move == 'S' or char_move == 'W':
                        delta = 1
                    else:  
                        delta = -1
                        is_negative_contribution = True
                
                current_objective_value += delta
                if is_negative_contribution:
                    negative_contributions_count += 1

                effective_changes = min(negative_contributions_count, k_changes)
                potential_value = current_objective_value + effective_changes * 2
                
                max_objective_value_so_far = max(max_objective_value_so_far, potential_value)
            
            return max_objective_value_so_far

        ans = 0
        ans = max(ans, calculate_max_objective_value(s, k, 'xy'))
        ans = max(ans, calculate_max_objective_value(s, k, 'xmy'))
        ans = max(ans, calculate_max_objective_value(s, k, 'mxy'))
        ans = max(ans, calculate_max_objective_value(s, k, 'mxmy'))

        return ans