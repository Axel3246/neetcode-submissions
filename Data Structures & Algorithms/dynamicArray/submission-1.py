class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.fixedArray = [None] * self.capacity

    # T: O(1)
    # S: O(1) extra space
    def get(self, i: int) -> int:
        return self.fixedArray[i]

    # T: 0(1)
    # S: O(1) extra space
    def set(self, i: int, n: int) -> None:
        self.fixedArray[i] = n

    # T: Best O(1), Worst O(N), Avg O(1)
    # S: Best O(1), Worst O(N)
    def pushback(self, n: int) -> None:
        print(self.fixedArray)
        if self.size == self.capacity:
            self.resize()

        self.fixedArray[self.size] = n
        self.size += 1
 
    # T: O(1)
    # S: O(1) extra space
    def popback(self) -> int:
        self.size -= 1
        return self.fixedArray[self.size]

    # T: O(n)
    # S: O(n) extra space
    def resize(self) -> None:
        self.capacity *= 2
        tempArray = [None] * self.capacity

        for i in range(self.size):
            tempArray[i] = self.fixedArray[i]

        self.fixedArray = tempArray    

    # T: O(1)
    # S: O(1) extra space
    def getSize(self) -> int:
        return self.size
    
    # T: O(1)
    # S: O(1) extra space
    def getCapacity(self) -> int:
        return self.capacity
