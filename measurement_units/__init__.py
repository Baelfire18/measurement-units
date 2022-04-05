class Unit():

    def __init__(self, value, unit=''):
        self.value = value
        self.power_unit = 1.0
        a = unit.find('**')
        if unit[a:] == '**1':
            self.unit = unit[:a]
        elif a == -1:
            self.unit = unit
        else:
            self.power_unit = float(unit[a + 2:])
            self.unit = unit[:a]

    def __str__(self):
        return f'{self.value} {self.unit}{f"**{self.power_unit}" if self.power_unit != 1 else ""}'
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        if self.unit == other.unit:
            return Unit(self.value + other.value, self.unit)
        raise TypeError('Units are not the same')

    def __sub__(self, other):
        if self.unit == other.unit:
            return Unit(self.value - other.value, self.unit)
        raise TypeError('Units are not the same')
    
    def __mul__(self, other):
        if self.unit == other.unit:
            return Unit(self.value * other.value, self.unit + f'**{self.power_unit * other.power_unit}')
        elif self.unit == '':
            return Unit(self.value * other.value, other.unit + f'**{other.power_unit}')
        elif self.other == '':
            return Unit(self.value * other.value, self.unit + f'**{self.power_unit}')
        raise TypeError('Units are not the same')
    
    def __truediv__(self, other):
        if self.unit == other.unit:
            return Unit(self.value / other.value, '')
        raise TypeError('Units are not the same')
    
    def __floordiv__(self, other):
        if self.unit == other.unit:
            return Unit(self.value // other.value, '')
        raise TypeError('Units are not the same')
    
    def __mod__(self, other):
        if self.unit == other.unit:
            return Unit(self.value % other.value, '')
        raise TypeError('Units are not the same')
    
    def __pow__(self, other):
        return Unit(self.value ** other, self.unit + f'**{self.power_unit * other}' if self.unit else '')

    def __res__(self, other):
        if self.unit == other.unit:
            return Unit(self.value - other.value, self.unit)

    def __lt__(self, other):
        if self.unit == other.unit:
            return self.value < other.value
        raise TypeError('Units are not the same')

    def __leq__(self, other):
        if self.unit == other.unit:
            return self.value <= other.value
        raise TypeError('Units are not the same')

    def __eq__(self, other):
        if self.unit == other.unit:
            return self.value == other.value
        raise TypeError('Units are not the same')
    
    def __neq__(self, other):
        if self.unit == other.unit:
            return self.value != other.value
        raise TypeError('Units are not the same')

    def __gt__(self, other):
        if self.unit == other.unit:
            return self.value > other.value
        raise TypeError('Units are not the same')
    
    def __ge__(self, other):
        if self.unit == other.unit:
            return self.value >= other.value
        raise TypeError('Units are not the same')


if __name__ == '__main__':

    a = Unit(4, 'km')
    b = Unit(6, 'km')
    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a == b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)

    """
    1. Keppler Law

    T**2 / a**3 = C
    """

    # 1.
    T_earth = Unit(365, 'days')
    a_earth = Unit(1, 'AU')
    T_mercury = Unit(88, 'days')

    a_mercury = ((T_mercury / T_earth )**2 * a_earth**3) **(1/3)
    print(f'{a_mercury = }')

