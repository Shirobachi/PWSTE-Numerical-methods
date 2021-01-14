# hryszko.dev simon@hryszko.dev ©️2021
def f(x):
	return 2 * pow(x, 3) + 5 * pow(x, 2) - 5 * x + 2


b = 0  # left border
a = 4  # right border
epsilon = .01 # quality

c = 0 # center of border

while abs(b-a) >= epsilon:
	c = (b-a)/2
	if f(c) == 0:
		break

	if f(a) * f(b) < 0:
		b = c
	else:
		a = c

print(f"Reult={c}")
