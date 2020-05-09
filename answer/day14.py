class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here
maximumDifference = 0

def computeDifference(self):
    for i in self.__elements:
        for j in self.__elements:
            tmpDifference = abs(i - j)
            if tmpDifference > self.maximumDifference:
                self.maximumDifference = tmpDifference

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)