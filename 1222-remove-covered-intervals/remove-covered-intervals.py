class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start time ascending, then by end time descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        prev_end = 0
        
        for _, end in intervals:
            if end > prev_end:
                ans += 1
                prev_end = end
                
        return ans
