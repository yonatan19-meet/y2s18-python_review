# Write your solutions for 1.5 here!
import random
class Superhero:
	def __init__(self, name, superpower, strength):
		self.name = name
		self.superpower = superpower
		self.strength = strength

	def printing(name, superpower):
		print(name)
		print(superpower)

	def power(self):
		work = random.randint(1,10)
		if self.strength > work:
			self.strength = self.strength - work
			print(self.strength)
		else:
			print(":(")

sw = Superhero("ho my", "jump", 12)
sw.power()


