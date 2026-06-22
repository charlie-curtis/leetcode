class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:


        seen = set()
        for w in startWords:
            li = [x for x in w]
            for i in range(26):
                li.append(chr(i + ord('a')))
                seen.add(''.join(sorted(li)))
                li.pop()
        return sum([1 if ''.join(sorted([x for x in t])) in seen else 0 for t in targetWords])
        