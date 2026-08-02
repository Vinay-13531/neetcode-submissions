class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = dict()
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for i in t:
            if i in letters:
                letters[i] -= 1
            else:
                return False
        for count in letters.values():
            if count != 0:
                return False
        return True