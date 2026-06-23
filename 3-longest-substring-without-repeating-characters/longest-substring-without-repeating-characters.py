class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start = 0
        max_len = 0
    
        for end in range(len(s)):
        # If character is a duplicate within the current window, move start
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
        # Record/update the position of the character
            char_map[s[end]] = end
        
        # Calculate maximum length
            max_len = max(max_len, end - start + 1)
        
        return max_len
    

    

        