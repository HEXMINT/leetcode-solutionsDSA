class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        left=0
        dic={}
        res=0
        for right in range(n):
            f_r=fruits[right]
            dic[f_r] = dic.get(f_r,0)+1
            while len(dic) > 2:
                f_l=fruits[left]
                dic[f_l]=dic.get(f_l)-1
                if dic[f_l] == 0:
                    del dic[f_l]
                left+=1
            res=max(abs(right-left)+1,res)
        return res