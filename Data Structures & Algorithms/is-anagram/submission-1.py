class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the length of both strings are different
            return False # they can't be annagrams and it will return false
        
        countS, countT = {}, {} # creates hashmaps for both strings

        for i in range(len(s)): # iterating through the length of string s
            countS[s[i]] = 1 + countS.get(s[i],0) # adds one to every occurance of the letter to the hashmap
            countT[t[i]] = 1 + countT.get(t[i],0) # adds one to every occurance of the letter to the hashmap

        return countS == countT # if each letter in the hashmap has the same number
        # of occurances then we return true if it does not then we return false
            
        