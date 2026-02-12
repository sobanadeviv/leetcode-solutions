#
# Problem: 9. Palindrome Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-number/
# Language: python3
# Date: 2026-02-12


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            num1=x
            y=0
            while(x>0):
                rem=x%10
                y=(y*10)+rem
                x=x//10
            if(num1==y):
                return True
            else:
                return False

        
