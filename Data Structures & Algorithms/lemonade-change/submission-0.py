class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        for b in bills:
            if 5==b:
                five+=1
            elif 10==b:
                ten+=1
                five-=1
            elif ten>0:
                ten-=1
                five-=1
            else:
                five-=3
            if five<0:
                return False
        return True
