class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        string = strs[0] + '�'
        for i in range(1, len(strs)):
            string += strs[i] + '�'
        return string
        


    def decode(self, s: str) -> List[str]:
        array = []
        substr = ''
        for i in range(len(s)):
            if s[i] == '�':
                array.append(substr)
                substr = ''
            else:
                substr += s[i]
        return array


