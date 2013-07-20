import math

# Gauss-Legendre algorithm
# http://en.wikipedia.org/wiki/Gauss-Legendre_algorithm
def gauss_legendre(n):
	a, b, t, p = 1, 1.math.sqrt(2), 0.25, 1 # Initial values for a, b, t, p
	for i in range(0, n):
		(an, bn, tn, pn) = gl_recurse(a, b, t, p)
		a, b, t, p = an, bn, tn, pn
	return math.pow(a+b, 2)/(4.0*t) # Approximation of pi

# Recursive Gauss-Legendre helper method
def gl_recurse(a, b, t, p):
	an = (a+b)*.5
	bn = math.sqrt(a*b)
	tn = t - p*math.pow(a - an, 2)
	pn = 2*p
	return an, bn, tn, pn