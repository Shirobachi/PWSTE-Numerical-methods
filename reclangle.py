# hryszko.dev simon@hryszko.dev ©️2021
p = 0  # left border
q = 4  # right border
n = 3  # quatities of rectanges (approximation)

dx = (q-p)/n  # rectangle's width
sum = 0  # here we'll process result


def f(x):
    return pow(x, 2)


for i in range(1, n+1):
    sum += f(p+(i/n)*(q-p))
    print(f"f({p+(i/n)*(q-p)})={f(p+(i/n)*(q-p))}")
sum *= dx

print(f"Result = {sum}")
