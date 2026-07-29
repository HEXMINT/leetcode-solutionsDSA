class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        right=n-1
        left=0
        res=[]
        while left<right:
            if numbers[left]+numbers[right]==target:
                res.append(left+1)
                res.append(right+1)
                break
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return res
