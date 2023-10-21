

class Gun:
    n = 1
    def shoot(self):
        if self.n % 2 == 1: print('pif')
        else: print('paf')
        self.n += 1
        
# INPUT DATA:

# TEST_1:
gun = Gun()

gun.shoot()
print()
# TEST_2:
gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
print()

# TEST_3:
gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
print()

# TEST_4:
gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()
gun1.shoot()
gun2.shoot()
gun1.shoot()        