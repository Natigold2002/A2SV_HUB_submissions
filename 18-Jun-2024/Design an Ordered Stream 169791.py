# Problem: Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.data=[""]*n
        self.ptr=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1]=value
        ans=[]
        while len(self.data)>self.ptr and self.data[self.ptr]!="" :
            ans.append(self.data[self.ptr])
            self.ptr+=1
        return ans


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)