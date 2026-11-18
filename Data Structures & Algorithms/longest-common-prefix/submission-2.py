class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        s = strs[0]
        for character_idx in range(len(s)):
            character = s[character_idx]
            for word_idx in range(1, len(strs)):
                word = strs[word_idx]
                
                if character_idx == len(word) or word[character_idx] != character:
                    return s[:character_idx]
                    
        return s  
