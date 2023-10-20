

class Knight:
    
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        
    def get_char(self):
        return 'N'
    
    def can_move(self, x_coord, y_coord):
        pass
    
    def move_to(self):
        pass
    
    def draw_board(self):
        pass        
    
    
    
# INPUT DATA:

# TEST_1:
knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

# TEST_2:
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

# TEST_3:
knight = Knight('c', 3, 'white')

knight.draw_board()

# TEST_4:
knight = Knight('e', 5, 'black')

knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()

# TEST_5:
knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()

# TEST_6:
knight = Knight('g', 7, 'black')
knight.draw_board()

# TEST_7:
knight = Knight('d', 8, 'white')
knight.draw_board()

# TEST_8:
knight = Knight('h', 1, 'black')
knight.draw_board()    