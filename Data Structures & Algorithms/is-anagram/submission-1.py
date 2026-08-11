class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for s_item in s:
            if s_item in s_hash:
                s_hash[s_item] += 1
            else:
                s_hash[s_item] = 1

        for t_item in t:
            if t_item in t_hash:
                t_hash[t_item] += 1
            else:
                t_hash[t_item] = 1
        
        return s_hash == t_hash
