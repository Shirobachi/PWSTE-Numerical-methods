# hryszko.dev simon@hryszko.dev ©️2021
import matplotlib.pyplot as plt


def f(t, y):
    return t + y

x1 = y1 = 0

step = 0.00001
p = 0
q = 2

x = []
y = []

while(x1 <= q):
    x1 += step
    y1 += step * f(x1, y1)

    x.append(round(x1, 2))
    y.append(round(y1, 3))

# for i in range(len(x)):
    # print(f"f({round(x[i],2)})={round(y[i],3)}\\\\")

print(f"f({q})={y[len(y)-1]}")

plt.plot(x, y)
plt.show()