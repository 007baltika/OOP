

class Gun():
    
    def __init__(self):
        self.shoots = 0
    
    def shoot(self):
        if self.shoots % 2 == 0: print('pif')
        else: print('paf')
        self.shoots += 1
        
    def shots_count(self):
        return self.shoots
    
    def shots_reset(self):
        self.shoots = 0
        
# INPUT DATA:

# TEST_1:
gun = Gun()

print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
print()
# TEST_2:
gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
print()
# TEST_3:
gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
print()
# TEST_4:
gun = Gun()

print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
print()
# TEST_5:
gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
print()
# TEST_6:
gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())
print()
# TEST_7:
gun = Gun()

gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
gun.shoot()            