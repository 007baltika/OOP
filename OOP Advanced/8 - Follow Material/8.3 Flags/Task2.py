# Реализуйте класс MovieGenres , описывающий флаг с жанрами кино. Флаг
# должен иметь пять элементов:
# • ACTION
# • COMEDY
# • DRAMA
# • FANTASY
# • HORROR

# Также реализуйте класс Movie , описывающий фильм. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • name — название фильма
# • genres — жанр фильма (элемент флага MovieGenres )

# Класс Movie должен иметь один метод экземпляра:
# • in_genre() — метод, принимающий в качестве аргумента жанр и
# возвращающий true , если фильм принадлежит данному жанру,
# или false в противном случае

# Экземпляр класса Movie должен иметь следующее неформальное строковое
# представление: <название фильма>

from enum import Flag, auto

class MovieGenres(Flag):
    
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()
    
class Movie():
    
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres
        
    def in_genre(self, genre):
        return genre in self.genres
    
    def __str__(self):
        return self.name
    

# INPUT DATA:

# TEST_1:
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie)
print()
# TEST_2:
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))
print()
# TEST_3:
movie = Movie('Scary movie', MovieGenres.COMEDY | MovieGenres.HORROR)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR))
print()
# TEST_4:
movie = Movie('Avengers', MovieGenres.FANTASY | MovieGenres.ACTION)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.FANTASY | MovieGenres.ACTION))
print(movie)
print()
# TEST_5:
movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
print(movie)
        