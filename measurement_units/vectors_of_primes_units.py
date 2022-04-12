N = 3
P = [2, 3, 5, 7, 11, 13]
units = {
"m": P[0],
"s": P[1]
}

def to_unit(value, unit):
	units_list = unit.split("*")
	units_value = 1
	for u in units_list:
		if u != "":
			units_value *= units[u]
	return [value, units_value]

class Unit(list):
	def __init__(self, value, unit):
		super().__init__(to_unit(value, unit))
	def __str__(self):
		return f"{self.value} {self.unit}"
	@property
	def value(self):
		return self[0]
	@property
	def unit(self):
		result  = []
		units_value = self[1]
		for key, value in units.items():
			if units_value % units[key] == 0:
				result += [key]
				
		return "*".join(result)
	def __add__(self, x):
		if self.unit == x.unit:
			return Unit(self.value + x.value, self.unit)
	def __mul__(self, x):
		return Unit(self.value * x.value, f"{self.unit}*{x.unit}")

if __name__ == "__main__":
	a = Unit(2, "m")
	b = Unit(5, "s")
	print(a + b)
	print(a * b)
	print(a * a)
