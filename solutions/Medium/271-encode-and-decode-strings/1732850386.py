#another approach to handle ALL unicode characters is to make # your special value, but also modify the input to escape any regular # to \# and any regular \ to be \\

'''
example: I am # a \# string##
encoded: I am \# a \\\# string\#\## (note we append a final # to mark the end of the string)

so if you ever see a # by itself, then split the string

sneaky case: I am a string #
encoded: I am a string \## (node we append a final # to mark the end of the string)
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        SPECIAL = "ƭ"
        return SPECIAL.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        SPECIAL = "ƭ"
        return s.split(SPECIAL)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))