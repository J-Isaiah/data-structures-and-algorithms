class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        result = []

        for word in strs:
            letters = sorted(word)
            key = "".join(letters)

            if key not in h:
                h[key] = [word]
                continue

            h[key].append(word)

        for key, item in h.items():
            result.append(item)

        return result


            
                
        