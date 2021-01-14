# hryszko.dev simon@hryszko.dev ©️2021
p = 0  # left border
q = 4  # right border
n = 5  # quatities of rectanges (approximation)
s = 0  # result
st = 0  # result of subset

dx = (q-p)/n  # rectangle's width


def f(x):
    return pow(x, 2)


i = 1  # iteration

while(i <= n):
    x = p+(i*dx)
    st += f(x-(dx/2))
    if i < n:
        s += f(x)
    i += 1

s = (dx/6)*(f(p)+f(q)+(2*s)+(4*st))

print(f"Result = {s}")
