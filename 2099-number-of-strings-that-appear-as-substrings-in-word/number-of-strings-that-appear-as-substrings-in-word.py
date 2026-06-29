class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns :
            if i in word :
                count += 1 
                print("Found!")
        return count 
