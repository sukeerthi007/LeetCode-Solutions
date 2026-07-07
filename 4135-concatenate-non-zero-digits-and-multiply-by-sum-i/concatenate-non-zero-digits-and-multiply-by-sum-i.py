class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert to string and filter out '0'
        digits = [c for c in str(n) if c != '0']
        
        # Handle the case where there are no non-zero digits
        if not digits:
            return 0
            
        # Convert remaining digits back into an integer
        x = int("".join(digits))
        
        # Calculate sum of digits
        digit_sum = sum(int(d) for d in digits)
        
        return x * digit_sum


            
