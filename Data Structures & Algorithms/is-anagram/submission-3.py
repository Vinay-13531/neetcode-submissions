from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)    
        '''
        counts = [0] * 26
        for char_s, char_t in zip(s,t):
            counts[ord(char_s) - 97] += 1
            counts[ord(char_t) - 97] -= 1
        return all(letter == 0 for letter in counts)
        '''