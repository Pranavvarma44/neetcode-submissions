class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an={}
        for words in strs:
            key="".join(sorted(words))

            if key not in an:
                an[key]=[]
            an[key].append(words)
        return list(an.values())
        