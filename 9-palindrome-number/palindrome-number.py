class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = 0
        original_x = x
        if x < 0 :
            return (False)
        while x > 0 :
            digit = x % 10
            reversed_x = reversed_x * 10 + digit 
            x = x // 10
        if original_x == reversed_x :
            return(True)
        else : 
            return(False)


