from collections import Counter
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hash_map=Counter(tasks)
        max_frequency=max(hash_map.values())
        count_max_frequency=list(hash_map.values()).count(max_frequency)
        total_partition_lengths=(max_frequency-1)*(n+1) + count_max_frequency
        return max(len(tasks),total_partition_lengths)
                    



        