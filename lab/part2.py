# Part 2 of the Python Review lab.
import math
def is_prime(x):
	is_num_prime = True
	for i in range(int(math.sqrt(x))):
		if x%(i+2)==0:
			is_num_prime = False
	return is_num_prime

def encode(x, y):
	if (1<y<250) and (500<x<1000):
		print(x*y)

def decode(coded_message):
	pass

encode(120, 750)
