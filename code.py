class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        d={}
        for num in nums:
            o=num%k
            if o==0:
                if o not in d:
                    d[num]=1
                else:
                    d[num]+=1
        print(d)
        g=len(nums)
        for i in range(1,g+2):
            print(k*i)
            if (k*i) not in d:
                print(k*i)
                return k*i


        
