

def Coordinates(*args):
    for arg in args:
        if  -90 <= arg[0] <= 90 and -180 <= arg[1] <= 180:
            print(True, end = '\n')
        else: print(False, end = '\n')
  
# Тестовые данные          
# print(Coordinates((75, 180), (90, -147.45), (77.111, 149.9999), (90, 180), (55.1, 249.9), (120, 150)))
# print()
# print(Coordinates((-90, -180),(-90.0, -180.0),(-90, 180),(90, -180),(90.0, 180.0)))
# print()
# print(Coordinates((-90.1, 1),(-90.2, 45),(10, 180.01),(1, 180.0004)))
# print()
# print(Coordinates((0, 0),(0.0, 0.0),(1.1, 1.1),(-43.33333333333333, -64.534895834579),(43.33333333333333, 64.534895834579),(11, 111)))
# print()
# print(Coordinates((226.16, -180.84),(-207.51, 226.18),(-279.64, -266.69),(283.64, 1.42),(-119.59, 40.77),(-140.26, -87.16)))
# print()
# print(Coordinates((221.99, -203.46),(-268.55, 157.83),(219.29, -6.51),(-183.96, 73.75),(30.37, -184.98),(-74.75, 30.1),(-79.66, 125.06),(104.14, 157.19),(-216.39, -236.77),(228.52, 65.93),(-243.64, -44.13),(196.12, 137.98)))
# print()
# print(Coordinates((25.65, -31.59),(271.68, -53.93),(168.62, 7.19),(-21.8, 101.3),(-20.95, -106.72),(-194.45, -243.06),(-288.46, -256.44),(101.69, -135.92),(27.2, 112.06),(159.17, -145.82),(-115.91, -94.18),(95.71, -140.5),(213.32, 225.35),(-163.19, -208.18)))
# print()
# print(Coordinates((261.4, -17.0),(210.67, -64.27),(-48.38, 149.44),(78.74, 105.72)))


