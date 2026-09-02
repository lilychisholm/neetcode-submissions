class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()
        for letter in s:
            if letter not in sdict:
                sdict[letter] = 1
            else:
                sdict[letter] += 1
        for letter in t:
            if letter not in tdict:
                tdict[letter] = 1
            else:
                tdict[letter] += 1
        if sdict == tdict:
            return True
        else:
            return False