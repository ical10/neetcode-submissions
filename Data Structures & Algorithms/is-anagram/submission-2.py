class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # immediately rejects strings of different lengths
        if len(s) != len(t):
            return False

        # use only one dictionary instead of two
        count = {}

        for char in s:
            # add a new char to count
            # or increment if it already exists
            count[char] = count.get(char, 0) + 1
        
        # then loop through t and compare with count
        for char in t:
            if char not in count:
                return False
            
            # decrement count of a char
            count[char] -= 1

            # remove char from count
            # if count falls to zero
            if count[char] == 0:
                del count[char]

        return not count