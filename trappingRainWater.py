# My solution to Goldman Sachs' "Trapping Rainwater" challenge

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1: 
            return 0
        leftInd = 0
        rightInd = 1
        totalWater = 0
        water = 0
        while rightInd != len(height)-1:
            #print(water)
            block1 = height[leftInd]
            block2 = height[rightInd]
            if block1 < block2: 
                leftInd = rightInd 
                totalWater += water
                water = 0
                rightInd += 1
                continue
            #rightInd += 1 

            if max(height[rightInd:]) < height[leftInd]: 
                block1 = max(height[rightInd:])
            
            if block1 > block2:      
                water += (block1 - block2) 

            rightInd += 1 

        totalWater += water
        return totalWater
