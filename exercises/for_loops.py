# Write your solution for 1.1 here!
import math
a=0
for i in range(101):
	a=a+i
print (a)

b=0
for i in range(101):
	if i%2==0:
		b=b+i
print(b)

for i in range(1000):
	if i%6==2:
		if (i**3)%5==3:
			print(i)