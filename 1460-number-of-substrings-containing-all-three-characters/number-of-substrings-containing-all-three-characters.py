class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        count = 0
    
        for i, char in enumerate(s):
            last[char] = i
            count += min(last['a'], last['b'], last['c']) + 1
        
        return count