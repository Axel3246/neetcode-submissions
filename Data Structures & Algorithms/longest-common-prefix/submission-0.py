class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(0, len(strs)-1):
            str1 = strs[i]
            for j in range(i+1, len(strs)):
                str2 = strs[j]
                print(str1, str2)
                currLongest = ""
                k = 0
                while k < min(len(str1), len(str2)):
                    if str1[k] != str2[k]:
                        break
                    currLongest += str1[k]
                    k += 1
                if len(currLongest) < len(longest):
                    longest = currLongest
                

    
        return longest
                    