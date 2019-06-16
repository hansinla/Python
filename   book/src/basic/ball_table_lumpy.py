from scitools.Lumpy import Lumpy
lumpy = Lumpy() 
lumpy.make_reference()

g = 9.81;  v0 = 5
dt = 0.25

def y(t):
    return v0*t - 0.5*g*t**2

def table():
    data = []  # store [t, y] pairs in a nested list
    t = 0
    while y(t) >= 0:
        data.append([t, y(t)])
        t += dt
    return data

data = table()

#lumpy.object_diagram()

for t, y in data:
    print '%5.3f  %5.3f' % (t, y)

# extract all y values from data:
y = [y for t, y in data]
print y
# find maximum y value:
ymax = 0
for yi in y:
    if yi > ymax:
        ymax = yi
print 'max y(t) =', ymax

lumpy.object_diagram()



