class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # This line initializes a hash set will depict if the num is seen
        for num in nums: # iterates through each num in the array and will give info
            if num in seen: # if the number is in the seen hash set it returns True
                return True   
            seen.add(num)
        return False
                
            
        
        