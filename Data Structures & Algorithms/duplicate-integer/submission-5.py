class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # This line initializes a hash set will depict if the num is seen
        for num in nums: # iterates through each num in the array and will give info
            if num in seen: # if the number is in the seen hash set it returns True
                return True # as soon as the code sees a duplicate, it returns true and stops running   
            seen.add(num) # if there is no duplicate (is not true), it adds the number to the hashmap
            # in order for it to be used in the next iteration
        return False # returns false after the for loop is run and if there are no duplicates
                
            
        
        