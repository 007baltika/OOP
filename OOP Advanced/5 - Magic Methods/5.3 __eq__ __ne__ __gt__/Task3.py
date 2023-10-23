# Экземпляры класса Month должны поддерживать все операции сравнения
# с помощью операторов ==, !=, >, <, >=, <= . Два Month объекта считаются
# равными, если их годы и порядковые номера месяцев совпадают. Month объект
# считается больше другого Month объекта, если его год больше. В случае если
# два Month объекта имеют равные года, большим считается тот, чей месяц
# больше. Методы, реализующие операции сравнения, должны уметь сравнивать
# как два Month объекта между собой, так и Month объект с кортежем из двух
# чисел, представляющих год и месяц.

from functools import total_ordering
@total_ordering
class Month:
    
    def __init__(self, year, month):
        self.year = year
        self.month = month
        
    def __repr__(self):
        return f'Month({self.year}, {self.month})'   
    
    def __str__(self):
        return f'{self.year}-{self.month}'
    
    def __eq__(self, other):
        
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
    
        elif isinstance(other, tuple):
            if len(other) == 2:
                return self.year == other[0] and self.month == other[1]
            return False
        return NotImplemented
    
    def __gt__(self, other):
        
        if isinstance(other, Month):
            if self.year != other.year:
                return self.year > other.year 
            return self.month > other.month
        
        elif isinstance(other, tuple):
            if len(other) == 2:
                if self.year != other[0]:
                    return self.year > other[0] 
                return self.month > other[1]
            return False
        
        return NotImplemented
    
# TEST_1:
print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))
print()
# TEST_2:
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))
print()
# TEST_3:
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))
print()
# TEST_4:
month = Month(2023, 4)
not_supported = ['04.2023', 4.0, 2023, True, {2023: 4}, {4, 2023}, False, (2023, 4, 'dont know')]
for obj in not_supported:
    print(month == obj)
print()
# TEST_5:
months = [Month(2014, 4), Month(2016, 8), Month(2006, 5), Month(2022, 8), Month(2014, 9), Month(2014, 9),
          Month(2002, 12), Month(2003, 8), Month(2016, 5), Month(2022, 5), Month(2019, 12), Month(2011, 2),
          Month(2005, 12), Month(2009, 8), Month(2023, 2), Month(2020, 5), Month(2020, 6), Month(2022, 4),
          Month(2000, 12), Month(2002, 5), Month(2012, 4), Month(2007, 1), Month(2008, 4), Month(2008, 1),
          Month(2000, 11), Month(2006, 8), Month(2011, 9), Month(2012, 12), Month(2015, 9), Month(2017, 12),
          Month(2016, 5), Month(2002, 1), Month(2015, 8), Month(2003, 4), Month(2005, 9), Month(2016, 9),
          Month(2009, 12), Month(2017, 4), Month(2020, 3), Month(2018, 12), Month(2008, 1), Month(2011, 11),
          Month(2004, 9), Month(2004, 9), Month(2002, 5), Month(2014, 6), Month(2023, 5), Month(2016, 11),
          Month(2002, 8), Month(2005, 12), Month(2002, 7), Month(2008, 3), Month(2015, 4), Month(2010, 10),
          Month(2014, 7), Month(2022, 9), Month(2001, 11), Month(2003, 1), Month(2000, 4), Month(2012, 7),
          Month(2004, 1), Month(2011, 6), Month(2012, 8), Month(2008, 9), Month(2005, 2), Month(2007, 8),
          Month(2012, 1), Month(2018, 7), Month(2022, 12), Month(2018, 11), Month(2001, 5), Month(2009, 10),
          Month(2000, 8), Month(2008, 4), Month(2018, 10), Month(2003, 5), Month(2020, 12), Month(2011, 3),
          Month(2003, 12), Month(2023, 3), Month(2003, 1), Month(2020, 7), Month(2019, 4), Month(2020, 2),
          Month(2005, 11), Month(2008, 7), Month(2013, 9), Month(2015, 4), Month(2004, 12), Month(2001, 2),
          Month(2003, 9), Month(2021, 6), Month(2020, 9), Month(2000, 10), Month(2021, 4), Month(2014, 11),
          Month(2016, 9), Month(2004, 12), Month(2015, 10), Month(2009, 1)]

print(sorted(months))
print(min(months))
print(max(months))
print()
# TEST_6:
print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))
print()
# TEST_7:
month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: 'one'}))    
    
     