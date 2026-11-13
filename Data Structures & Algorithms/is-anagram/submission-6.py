class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        for str in s:
            freq1[str] = freq1.get(str,0) + 1
        
        freq2 = {}
        for str in t:
            freq2[str] = freq2.get(str,0) + 1
        
        if freq1 != freq2:
            return False
        return True
