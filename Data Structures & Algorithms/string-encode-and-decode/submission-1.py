class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            # must store string length so we can decode later
            result.append(str(len(s)))
            # replace , with #
            result.append("#")
            # then append to result
            result.append(s)
        
        # transform array into string
        return "".join(result)
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # find the separator after the length
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            # move past "#"
            i = j + 1

            # read exactly `length` characters
            result.append(s[i:i + length])
            i += length
        return result

