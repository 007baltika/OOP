

class NewInt(int):
    
    def repeat(self, n = 2):
        perem = str(self) * n
        return perem
    
    def to_bin(self):
        return format(self, 'b')
    
a = NewInt(9)
print(a.repeat())
d = NewInt(a+5)
print(d.repeat(3)) 
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())  
NewInt()