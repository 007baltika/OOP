

# Реализуйте абстрактный класс ChessPiece , описывающий шахматные фигуры


from abc import ABC, abstractclassmethod

class ChessPiece(ABC):
    
    def __init__(self, horizontal, vertical):
        self.range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    def can_move(self):
        pass
    
class King(ChessPiece):
    
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.horizontal = horizontal
        self.vertical = vertical
        
    def can_move(self, horizontal, vertical):
        if (horizontal in self.range) and (vertical in range(1, 9)):
            if abs(self.range.index(self.horizontal) - self.range.index(horizontal)) <= 1 and abs(self.vertical - vertical) <= 1:
                return True
            else: return False
        else: return False
        
class Knight(ChessPiece):
    
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.horizontal = horizontal
        self.vertical = vertical
    
    def can_move(self, horizontal, vertical):
        
        if (abs(self.range.index(self.horizontal)-self.range.index(horizontal))==2 and abs(self.vertical-vertical)==1) or (abs(self.vertical-vertical)==2 and abs(self.range.index(self.horizontal)-self.range.index(horizontal))==1):
            return True
        else:
            return False
            
# INPUT DATA:

# TEST_1:
king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))
print()
# TEST_2:
knight = Knight('c', 3)

print(knight.can_move('e', 5))
print(knight.can_move('e', 4))
print()
# TEST_3:
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))
print()
# TEST_4:
knight = Knight('h', 8)

print(knight.can_move('h', 8))
print(knight.can_move('a', 6))
print(knight.can_move('a', 1))
print(knight.can_move('g', 6))
print()
# TEST_5:
knight = Knight('a', 1)

for horizontal in 'abcdefg':
    for vertical in range(1, 9):
        print(f'{horizontal}{vertical}', knight.can_move(horizontal, vertical))
print()
# TEST_6:
king = King('a', 1)

for horizontal in 'abcdefg':
    for vertical in range(1, 9):
        print(f'{horizontal}{vertical}', king.can_move(horizontal, vertical))
print()
# TEST_7:
kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
                      king.can_move(horizontal, vertical))
print()
# TEST_8:
knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for knight in knights:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if knight.can_move(horizontal, vertical):
                print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal}{vertical}',
                      knight.can_move(horizontal, vertical))            
