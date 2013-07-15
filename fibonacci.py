import math

def fib(n):
	phi = (1 + math.sqrt(5))/2
	psi = -math.pow(phi, -1)
	return int((math.pow(phi, n) - math.pow(psi, n))/math.sqrt(5))