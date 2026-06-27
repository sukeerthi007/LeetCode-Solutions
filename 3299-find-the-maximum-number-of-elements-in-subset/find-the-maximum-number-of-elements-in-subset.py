class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        from collections import Counter
        # 1. Count the frequency of each number
        counts = Counter(nums)
        max_length = 1
    
        # 2. Handle the special case for 1
        if 1 in counts:
            ones_count = counts[1]
        # Must be an odd number of elements to form the pattern [1, 1, 1]
            if ones_count % 2 == 0:
                max_length = max(max_length, ones_count - 1)
            else:
                max_length = max(max_length, ones_count)
            
    # 3. Process all other base numbers > 1
        for x in counts:
            if x == 1:
                continue
            
            current_length = 0
            current_base = x
        
        # Keep squaring as long as we have at least 2 copies to place on both sides
            while current_base in counts and counts[current_base] >= 2:
                current_length += 2
                current_base = current_base ** 2
            
        # The peak element of the pattern only needs a frequency of 1
            if current_base in counts and counts[current_base] >= 1:
                current_length += 1
            else:
            # If the peak didn't exist at all, we must remove 1 from the sequence 
            # to make sure the topmost available square acts as the odd peak element
                current_length -= 1
            
            max_length = max(max_length, current_length)
        
        return max_length
