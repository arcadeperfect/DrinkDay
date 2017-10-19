class Animal:
	def __init__(self, Name='', age=0, arms=0):
		self.Name = Name
		self.age = age
		self.arms = arms

	def GetName(self):
		return self.Name
	def SetName(self, Name):
		self.Name = Name

x = Animal('jake', 28, 4)

print x.arms
