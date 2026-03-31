class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for string in strs:
            key=tuple(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key]=[string]
        return list(anagrams.values())
