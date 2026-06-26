class Solution:
    def romanToInt(self, s: str) -> int:
    # 1. Map symbols to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        total = 0
    
    # 2. Loop through string up to the second-to-last character
        for i in range(len(s) - 1):
        # 3. Check if subtraction rule applies
            if roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
            
    # 4. Always add the final character's value
        total += roman_map[s[-1]]
    
        return total
