class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, from start and end
        i = 0
        j = len(s) - 1
        for _ in range(len(s)):
            if not s[i].isalnum():
                i += 1
                continue  
            if not s[j].isalnum():
                j -= 1
                continue
            print(s[i], s[j])
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

        