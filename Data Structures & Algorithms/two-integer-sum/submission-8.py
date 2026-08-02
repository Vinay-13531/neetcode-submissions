class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #time optimized
        '''
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
            
            seen[num] = i
            '''
        #space optimized
        num_with_index = [(num, i) for i, num in enumerate(nums)]
        
        num_with_index.sort(key=lambda x: x[0])
        
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = num_with_index[left][0] + num_with_index[right][0]
            
            if current_sum == target:
                if num_with_index[left][1] < num_with_index[right][1]:
                    return [num_with_index[left][1], num_with_index[right][1]]
                return [num_with_index[right][1], num_with_index[left][1]]
            elif current_sum < target:
                left += 1   
            else:
                right -= 1