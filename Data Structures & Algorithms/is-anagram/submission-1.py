from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getCharFreq(s) == self.getCharFreq(t)
        
    def getCharFreq(self, s: str):
        char_freq = defaultdict(int)
        for ch in s:
            char_freq[ch] += 1
        return char_freq