class Codec:
    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s):
        result = []
        i = 0

        
