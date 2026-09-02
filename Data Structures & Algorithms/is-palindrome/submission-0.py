class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        middle = 0
        if len(s) % 2 == 0:
            middle = len(s)/2
        else:
            middle = int((len(s)/2)+0.5)
        front = 0
        back = len(s)-1
        while front != middle:
            if s[front] != s[back]:
                return False
            else:
                front += 1
                back -= 1
        return True