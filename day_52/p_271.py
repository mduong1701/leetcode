from re import I


class Codec:
    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i
            
            while j != "#":
                j += 1

            length = int(s[i : j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return result

