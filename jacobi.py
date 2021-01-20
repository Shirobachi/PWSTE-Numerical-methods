# hryszko.dev simon@hryszko.dev ©️2021

def f(x, y, z):
    Rx = (y-2*z+12)/5
    Ry = (-3*x+2*z-25)/8
    Rz = (-x-y+6)/4

    return [Rx, Ry, Rz]

eps = 0.000000000000001

x = y = z = 0
sub = -1

while sub == -1 or sub >= eps:
    temp = f(x, y, z)

    sub = max(abs(temp[0]-x), abs(temp[1]-y),abs(temp[2]-z))

    x = temp[0]
    y = temp[1]
    z = temp[2]

print(f"x={x}\ty={y}\tz={z}")