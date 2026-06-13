class Solution: # brute force , most intuitive way, creates nested loop to check each value against another
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)): # iterates through each number
            for j in range (i + 1, len(nums)):# iterates through each number after the outer loop num
                if nums[i] + nums[j] == target: # checks if the values added together equal the target
                    return [i,j] # if they do add together, it returns both the indexs
            
        