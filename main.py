import matplotlib.pyplot as plt

#CLASSES
class Vector2:
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
        self.__check()
    
    def __check(self):
        types = (int,float)
        if type(self.x) not in types:
            raise Exception(f"'{self.x}' is not a number")
        if type(self.y) not in types:
            raise Exception(f"'{self.y}' is not a number")
    
    #Operations
    def __add__(self,other):
        return Vector2(self.x + other.x,self.y + other.y)
    
    def __sub__(self,other):
        return Vector2(self.x - other.x,self.y - other.y)
    
    def __mul__(self,other):
        if type(other) == Vector2:
            return Vector2(self.x * other.x,self.y * other.y)
        else:
            return Vector2(self.x * other,self.y * other)
    ################################################################

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"
    
    def __iter__(self):
        return iter((self.x,self.y))
    
class line:
    def __init__(self,finish : Vector2, start : Vector2 = Vector2(0,0)) -> None:
        self.start = start
        self.finish = finish
        self.__check()
    
    def __check(self):
        
        if type(self.start) != Vector2:
            raise Exception(f"'{self.start}' is not an object of the class {Vector2}")
        if type(self.finish) != Vector2:
            raise Exception(f"'{self.finish}' is not an object of the class {Vector2}")
    #Operators
    def __add__(self,other):
        return line(self.finish + other.finish, self.start + other.start)

    def __sub__(self,other):
        return line(self.finish - other.finish, self.start - other.start)
    
    def __mul__(self,other):
        if type(other) == line:
            return line(self.finish * other.finish, self.start * other.start)
        else:
            return line(self.finish * other, self.start * other)
    
    #################################################
    def __str__(self):
        return f"{self.start} -> {self.finish}"
    def __repr__(self):
        return f"{self.start} -> {self.finish}"

class Draw:
    #want to change how this works
    def __init__(self,fig = plt.figure()) -> None:
        self.Plot = plt
        self.fig = fig
        self.ax = self.fig.add_subplot(1,1,1)

    def Line(self,*lines):
        for Line in lines:
            if type(Line) != line: raise Exception(f"'{Line}' is not an object of the class ({line})")
            x1,y1 = Line.start
            x2,y2 = Line.finish
            self.ax.plot((x1,x2),(y1,y2))
    
    def Point(self,*points):
        for point in points:
            if type(point) != Vector2: raise Exception(f"'{point}' is not an object of the class ({Vector2})")
            x,y = point
            self.ax.plot(x,y,'ro')

    def Triangle(self,*Vectors,offset = Vector2(0,0)):
        if len(Vectors) != 3:
            raise Exception("Triangles have 3 sides")
        l1 = line(Vectors[1] + offset, Vectors[0] + offset)
        l2 = line(Vectors[2] + offset, Vectors[1] + offset)
        l3 = line(Vectors[0] + offset, Vectors[2] + offset)
        self.Lines(l1,l2,l3)

    def Square(self,size,offset = Vector2(0,0)):
        if size < 0:
            raise Exception("Shapes can't have negative size")
        v1 = Vector2(0,0) + offset
        v2 = Vector2(0,size) + offset
        v3 = Vector2(size,size) + offset
        v4 = Vector2(size,0) + offset
        l1 = line(v2,v1)
        l2 = line(v3,v2)
        l3 = line(v4,v3)
        l4 = line(v4,v1)
        self.Line(l1,l2,l3,l4)

class Statistics:
    def __init__(self,List) -> None:
        self.items = List
        self.Mean = self.__mean()
        self.Median = self.__median()
        self.Mode = self.__mode()
        self.StandardDeviation = self.__standard_dev()
        self.Min,self.Max = self.__MinMax()
        self.plt = plt
        self.fig = self.plt.figure()
        self.ax1 = self.fig.add_subplot(2,1,1)
        self.ax2 = self.fig.add_subplot(2,1,2)

    def __str__(self) -> str:
        return f"Mean: {self.Mean}\nMedian: {self.Median}\nMode: {self.Mode}\nStandard Deviation: {self.StandardDeviation}\nMin: {self.Min}\nMax: {self.Max}"

    def __MinMax(self):
        min = self.items[0]
        max = self.items[0]
        for i in self.items:
            if i > max:
                max = i
            if i < min:
                min = i
        return min,max

    def __mean(self,List = None):
        if List == None: List = self.items
        s = 0
        for item in List:
            s += item
        return s / len(List)

    def __median(self,List = None):
        if List == None: List = self.items
        NewList = list(List)
        NewList.sort()
        if (len(NewList)) % 2 == 0:
            L1 = NewList[int((len(NewList)) / 2)]
            L2 = NewList[int((len(NewList) - 2 ) / 2)]
            return self.__mean((L1,L2))
        else:
            return (NewList[int((len(NewList) - 1) / 2)])
        
    def __mode(self,List = None):
        if List == None: List = self.items
        unique = []
        unique = [i for i in List if i not in unique]
        unique.sort()
        unique_q = [0 for _ in range(len(unique))]
        Index = -1
        for i in unique:
            Index += 1
            for j in List:
                if i == j:
                    unique_q[Index] += 1
        Index = -1
        Saved_Index = 0
        for i in unique_q:
            Index += 1
            if i > unique_q[Saved_Index]:
                Saved_Index = Index
        return unique[Saved_Index]

    def __standard_dev(self,List = None):
        if List == None: List = self.items
        av = self.__mean(List)
        dev = []
        for i in List:
            dev.append((i - av)**2)
        return (self.__mean(dev)) ** (1/2)

    def Graph(self):
        x = ["Mean","Median","Mode","Standard Deviation"]
        y = [self.Mean,self.Median,self.Mode,self.StandardDeviation]


        self.ax1.bar(x,y,width= .4,color='slategray',edgecolor='dimgray')
        for index,value in enumerate(y):
            self.ax1.text(index - .08,value + .05,str("≈% .2f" % value))
        
        self.ax2.plot(self.items)
        self.ax2.axhline(y=self.Min,linestyle = '--',label = "Min")
        self.ax2.axhline(y=self.Max,linestyle = '--',label = "Max",color='r')
        self.ax2.axhline(y=self.Mean + self.StandardDeviation,linestyle = ':',label = "Standard Deviation",color = 'purple')
        self.ax2.axhline(y=self.Mean - self.StandardDeviation,linestyle = ':',color = 'purple')
        self.ax2.axhline(y=self.Mean,linestyle = ':',label = "Mean",color = 'black')
        #Needs Fixing
        self.ax2.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
########################################################################
#Functions
def Sum(i:int,n:int,func):
    s = 0
    for j in range(i,n+1):
        s += func(j)
    return s

def Factorial(n):
    """Returns the factorial of given number."""
    fact = 1
    for i in range (1,n+1):
        fact *= i
    return fact
    

def Choose(n,k):
    """Returns the binomial coefficient of n and k"""
    return Factorial(n) / (Factorial(k) * Factorial(n - k))

def BinomialProbability(n,x,p):
    """
    Returns the Binomial Probability of n, x and p where:

    The number of trials, denoted by 'n'.
    
    The probability of success on each trial, denoted by 'p'.
    
    The desired number of successes, denoted by 'x'.
    """
    return (Choose(n,x)) * (p**x) * ((1 - p)**(n - x))

"""
Python already has MOD "%" :)
def MOD(Dividend,Divisor):
    if Divisor == 0:
        raise ZeroDivisionError("division by zero")
    if Dividend < 0 and Divisor < 0:
        MOD(Dividend * -1, Divisor * -1)
    elif Dividend < 0:
        return MOD(Dividend * -1,Divisor) * -1
    elif Divisor < 0:
        return MOD(Dividend,Divisor * -1) * -1
    return Dividend - Divisor * (Dividend // Divisor)
"""
#This is here for testing
if __name__ == "__main__":
    v1 = Vector2(10,5)
    l1 = line(v1)
    d = Draw()
    d.Line(l1)
    d.Plot.show()
    print(l1 + l1)
########################################################################
