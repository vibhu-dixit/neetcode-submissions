class FreqStack:

    def __init__(self):
        self.cnt={}
        self.maxcount=0
        self.stacks={}

    def push(self, val:int)-> None:
        valuecount=self.cnt.get(val,0)+1
        self.cnt[val]=valuecount
        if valuecount>self.maxcount:
            self.maxcount=valuecount
            self.stacks[valuecount]=[]
        self.stacks[valuecount].append(val)
    
    def pop(self)->int:
        result=self.stacks[self.maxcount].pop()
        self.cnt[result]-=1
        if not self.stacks[self.maxcount]: # if the max element list got empty
            self.maxcount-=1
        return result