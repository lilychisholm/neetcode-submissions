class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = dict()
        for word in strs:
            if tuple("".join(sorted(word))) in words:
                words[tuple("".join(sorted(word)))].append(word)
            else:
                words[tuple("".join(sorted(word)))] = [word]
        res = list(words.values())
        return res




        