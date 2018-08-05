# Part 1 of the Python Review lab.

def hello_world():
	print("hello_world")

def greet_by_name(name):
	print("hello " + name)

def encode(x):
	return (x*3953531)

def decode(coded_message):
	y = coded_message/3953531
	print (y)
	return (y)

decode(encode(5))
greet_by_name("yonatan")