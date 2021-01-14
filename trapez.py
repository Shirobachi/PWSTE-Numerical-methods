# hryszko.dev simon@hryszko.dev ©️2021
p = 0  # left border
q = 4  # right border
n = 5  # quatities of rectanges (approximation)

dx = (q-p)/n  # rectangle's width
sum = 0  # here we'll process result
print(f"dx={dx}")


def f(x):
    return pow(x, 2)


for i in range(n):
    a = f(p+(i/n)*(q-p))
    b = f(p+((i+1)/n)*(q-p))
    sum += (a+b)/2
    print(f"f({p+(i/n)*(q-p)}={a}")
    print(f"f({p+((i+1)/n)*(q-p)}={b}")

sum *= dx

print(f"Result = {sum}")
