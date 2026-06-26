class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #Import Counter
        from collections import Counter
        #Count the characters
        count = Counter(text)
        #Calculate the minimum instances
        result = min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
        return result
