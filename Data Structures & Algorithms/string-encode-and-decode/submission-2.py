class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            # must save string length so we can decode later
            result.append(str(len(s)))
            # use delimiter to separate length and string
            result.append("#")
            # then append encoded string
            result.append(s)

        # join and convert array into string
        return "".join(result)
        
    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        # create loop until the end of encoded string
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # get the `length` of an encoded string
            length = int(s[i:j])

            # move past "#"
            i = j + 1

            # get the encoded string, from i until `length`
            result.append(s[i:i + length])
            i += length

        return result


