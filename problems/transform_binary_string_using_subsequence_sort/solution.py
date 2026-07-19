from collections import Counter
class Solution(object):
    def transformStr(self, s, strs):
        """
        :type s: str
        :type strs: List[str]
        :rtype: List[bool]
        """
        n = len(s)
        target_ones = s.count('1')        
        pref_s = [0] * (n + 1)
        for i in range(n):
            pref_s[i + 1] = pref_s[i] + (1 if s[i] == '1' else 0)            
        ans = []        
        for target in strs:
            fixed_ones = 0
            q_indices = []        
            for i in range(n):
                if target[i] == '1':
                    fixed_ones += 1
                elif target[i] == '?':
                    q_indices.append(i)       
            needed_ones_from_q = target_ones - fixed_ones
            if needed_ones_from_q < 0 or needed_ones_from_q > len(q_indices):
                ans.append(False)
                continue   
            t_list = list(target)
            ones_start_idx = len(q_indices) - needed_ones_from_q         
            for idx, pos in enumerate(q_indices):
                t_list[pos] = '1' if idx >= ones_start_idx else '0'   
            possible = True
            curr_ones_t = 0
            for j in range(n):
                if t_list[j] == '1':
                    curr_ones_t += 1
                if curr_ones_t > pref_s[j + 1]:
                    possible = False
                    break                 
            ans.append(possible)     
        return ans
            
            
            
            
            
        