# Write your solution for 1.4 here!
import math
def is_prime(x):
	is_num_prime = True
	for i in range(int(math.sqrt(x))):
		if x%(i+2)==0:
			is_num_prime = False
	return is_num_prime

check=is_prime(17)
check2=is_prime(157)
check3=is_prime(93133)
print(check)
print(check2)
print(check3)
