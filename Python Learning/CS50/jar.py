class Jar:
    def __init__(self, capacity=12):
        if (capacity<0):
            raise ValueError
        self._capacity=capacity
        self._size=0

    def __str__(self):
        return(self.size*"🍪")

    def deposit(self, n):
        if n>self.capacity:
            raise ValueError

        if(self.size+n>self.capacity):
            raise ValueError
        self._size=self._size+n


    def withdraw(self, n):
        if(n>self.size):
            raise ValueError
        else:
            self._size=self._size-n


    @property
    def capacity(self):
        return(self._capacity)

    @property
    def size(self):
        return(self._size)

jar=Jar()
print(jar.__str__())