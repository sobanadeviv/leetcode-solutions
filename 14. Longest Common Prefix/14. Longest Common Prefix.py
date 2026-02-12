#
# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/?source=submission-ac
# Language: python3
# Date: 2026-02-12


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=len(strs[0])
        for z in strs:

            a=len(z)
            if min_len>a:
                min_len=a

        list1=""
        for y in range(0,min_len):
            current_check=strs[0][y]
            for word in strs[1:]:
                if(current_check!=word[y]):
                    return list1
            list1+=current_check
        return list1    
            
