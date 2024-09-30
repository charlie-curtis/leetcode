class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        #message = set(message)
        bannedWords = set(bannedWords)

        filtered = [x for x in message if x in bannedWords]
        return len(filtered) >= 2
        