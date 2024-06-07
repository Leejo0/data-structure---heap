class heap:
    def __init__(self,list):
        if list == None:
            self.__A = []
        else:
            self.__A = list

    def insert(self,x):
        self.__A.append(x)
        self.__percolateup(len(self.__A)-1)

    def __percolateup(self,i:int):
        parent = (i-1)//2
        if i>=0 and self.__A[i]>self.__A[parent]:
            self.__A[i],self.__A[parent] = self.__A[parent],self.__A[i]
            self.__percolateup(parent)

    def isempty(self) -> bool:
        return len(self.__A)==0

    def deletemax(self):
        if not self.isempty():
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolatedown(0)
            return max
        else:
            return None
        
    def __percolatedown(self,i:int):
        child = 2*i-1
        right = 2*i+2
        if child <= len(self.__A)-1:
            if right <= len(self.__A)-1 and self.__A[right] > self.__A[child]:
                child = right
            if self.__A[child] > self.__A[i]:
                self.__A[i],self.__A[child] = self.__A[child],self.__A[i]
                self.__percolatedown(child)

    def buildheap(self):
        for i in range((len(self.__A)-2)//2,-1-1):
            self.__percolatedown(i)

    def clear(self):
        self.__A = []

    def printheap(self):
        print(self.__A)
        

h1 = heap([60,0,43,128,4,13,52,100])
h1.buildheap()
h1.clear()
h1.insert(18)
h1.insert(3)
h1.insert(45)
h1.insert(102)
h1.insert(0)
h1.insert(32)
h1.printheap()
h1.deletemax()
h1.printheap()



