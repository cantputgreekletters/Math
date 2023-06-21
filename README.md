1. [Math](#Math)
2. [Classes](#Classes)
    1. [Vector2](#Vector2)
    2. [Line](#Line)
    3. [Draw](#Draw)
        1. [Draw.Line](#Draw.Line)
        2. [Draw.Triangle](#Draw.Triangle)
        3. [Draw.Square](#Draw.Square)
        4. [Draw.Point](#DrawPoint)
    4. [Statistics](#Statistics)
        1.[Statistics.Graph](#Statistics.Graph)
3. [Functions](#Functions)
    1. [Sum](#Sum)
    2. [MOD](#MOD)
# Math <a name="Math"></a>
 Various Math functions and classes that one might want to use. This "Library" is made mostly for fun other than to be actually used.

External libraries used: matplotlib.pyplot

If you wish to use it for your personal code or to modify it be free to do it.



# Classes <a name="Classes"></a>
## Vector2 <a name="Vector2"></a>
By using two numbers int or float you make a vector (They are 2D).

Vector2(x,y)

x,y need to be numbers

You can add,subtract, iterate a Vector2 object and use them in the Draw Class

## Line  <a name="Lines"></a>
By using two Vectors you can make a line

line(finish,start = Vector2(0,0))

start,finish need to be Vector2 Objects

You can use a line in the Draw Class

## Draw(fig = plt.figure()) <a name="Draw"></a>
self.Plot = plt
self.fig = fig
self.ax = self.fig.add_subplot(1,1,1)

This class has various methods that are used to draw shapes using matplotlib.

### Draw.Line(*lines) <a name="Draw.Line"></a>
You can pass an infinite ammount of line objects and they are drawn in matplotlib.

### Draw.Triangle(*vectors,offset = Vector2(0,0)) <a name="Draw.Triangle"></a>
You can pass three Vector2 objects and make a triangle with this method and set an offset to the triangle

### Draw.Square(size,offset = Vector2(0,0)) <a name="Draw.Square"></a>
You can pass a number and a square is drawn with the size that you passed and set an offset to the squarea.

### Draw.Point(*points) <a name="Draw.Point"></a>
You can pass an infinite amount of objects of the class Vector2 and visualize them in matplotlib.

## Statistics(List) <a name="Statistics"></a>
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
### Statistics.Graph()
Displays a graph that includes some statistical data of the list.
The user can customize further and show the graph by using the "Statistics.fig", "Statistics.ax1" and "Statistics.ax2" attributes.
use -> Statistics.plt.show() to display the graph if you haven't imported matplotlib.
# Functions <a name="Functions"></a>
### Sum(i,n,func) <a name="Sum"></a>
It works just like the Σ in maths.

i,n need to be int

'func' example: def F(x): return x^2

