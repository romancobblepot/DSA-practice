class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        vowels={'a','e','i','o','u'}
        vowel=[0]
        for i in range(n):
            if word[i] in vowels:
                vowel.append(i)
        vowel.append(n-1)
        total=0
        for j in range(1,len(vowel)-1):
            prev_vowel_pos=vowel[j-1]
            next_vowel_pos=vowel[j+1]
            right_side=n-vowel[j]
            left_side=vowel[j]+1
            total+=(left_side*right_side)
        return total



        
        