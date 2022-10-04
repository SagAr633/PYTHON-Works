# Global & Local Variable
y=6
def printx():
    global y
    y=y+2
    print(y)
printx()

z=99
def printz():
    global z
    z=z+1
    print(z)
printz()
