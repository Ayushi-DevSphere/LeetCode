from sortedcontainers import SortedList
import itertools

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Count initial inversions
        inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))
        
        # Build linked list structure
        nextIndices = [i + 1 for i in range(n)]
        prevIndices = [i - 1 for i in range(n)]
        
        # Store all pair sums as (sum, index) in sorted order
        pairSums = SortedList((a + b, i) 
                               for i, (a, b) in enumerate(itertools.pairwise(nums)))
        
        while inversionsCount > 0:
            ans += 1
            
            # Get minimum pair sum
            pairSum, currIndex = pairSums.pop(0)
            nextIndex = nextIndices[currIndex]
            prevIndex = prevIndices[currIndex]
            
            # Update left neighbor's pair sum
            if prevIndex >= 0:
                oldPairSum = nums[prevIndex] + nums[currIndex]
                newPairSum = nums[prevIndex] + pairSum
                pairSums.discard((oldPairSum, prevIndex))
                pairSums.add((newPairSum, prevIndex))
                
                # Update inversions for left side
                if nums[prevIndex] > nums[currIndex]:
                    inversionsCount -= 1
                if nums[prevIndex] > pairSum:
                    inversionsCount += 1
            
            # Handle right neighbor removal
            if nums[nextIndex] < nums[currIndex]:
                inversionsCount -= 1
            
            # Update right neighbor's pair sum
            nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
            if nextNextIndex < n:
                oldPairSum = nums[nextIndex] + nums[nextNextIndex]
                newPairSum = pairSum + nums[nextNextIndex]
                pairSums.discard((oldPairSum, nextIndex))
                pairSums.add((newPairSum, currIndex))
                
                # Update inversions for right side
                if nums[nextNextIndex] < nums[nextIndex]:
                    inversionsCount -= 1
                if nums[nextNextIndex] < pairSum:
                    inversionsCount += 1
                
                prevIndices[nextNextIndex] = currIndex
            
            # Merge: update current position and skip next
            nextIndices[currIndex] = nextNextIndex
            nums[currIndex] = pairSum
        
        return ans
