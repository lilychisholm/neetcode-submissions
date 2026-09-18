class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #keep count of letters specific to s1
        #keep hash table of them too
        #increment and decrement hash table values as pointers move
        #pointers are window of fixed size
        #remove letter from left pointer, add letter at right pointer
        #count first len(s1) letters to begin hash table

        if len(s1) > len(s2):
            return False

        word = dict()
        word_counter = dict()
        for i in range(len(s1)):
            if s1[i] in word:
                word[s1[i]] += 1
            else:
                word[s1[i]] = 1

            if s2[i] in word_counter:
                word_counter[s2[i]] += 1
            else:
                word_counter[s2[i]] = 1

        left = 0
        right = len(s1) - 1
        while right < len(s2):
            print(left, right)
            print(word_counter, word)
            if word_counter == word:
                return True
            else:
                right += 1
                if right < len(s2):
                    if s2[right] in word_counter:
                        word_counter[s2[right]] += 1
                    else:
                        word_counter[s2[right]] = 1
                word_counter[s2[left]] -= 1
                if word_counter[s2[left]] == 0:
                    del word_counter[s2[left]]
                left += 1
                
                
                
                


        return False
        
        