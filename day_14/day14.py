class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        difference = 0
        for n in self.__elements:
            for k in self.__elements:
                a = abs(n - k)
                if a > difference:
                    difference = a
        self.maximumDifference = difference
        return difference
