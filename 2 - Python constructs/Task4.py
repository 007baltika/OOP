# Артур владеет небольшой коллекцией карточек с покемонами, среди которых
# встречаются дубликаты. Он хочет оставить по одной карточке каждого типа, а
# остальные продать.Напишите программу, которая определяет, сколько
# дубликатов из своей коллекции Артур может продать.

def Pocemon(*args):
    return len(args) - len(set(args))

print(Pocemon('Pichu', 'Pichu', 'Tyrogue', 'Pichu', 'Combee', 'Marill', 'Tyrogue'))
print(Pocemon('Tyrogue', 'Pichu', 'Combee'))
print(Pocemon('Combee', 'Combee', 'Marill', 'Marill', 'Pichu', 'Pichu', 'Tyrogue', 'Tyrogue'))
print(Pocemon('Combee', 'Pichu', 'Tyrogue', 'Marill', 'Marill', 'Marill', 'Marill', 'Marill', 'Marill', 'Marill'))
print(Pocemon('Combee', 'Combee', 'Combee', 'Combee', 'Combee', 'Combee', 'Combee', 'Combee', 'Combee', 'Combee'))
print(Pocemon('Combee', 'Pichu', 'Tyrogue', 'Marill', 'Combee', 'Pichu', 'Tyrogue', 'Marill', 'Combee', 'Pichu', 'Tyrogue', 'Marill', 'Combee', 'Pichu', 'Tyrogue', 'Marill', 'Combee', 'Pichu', 'Tyrogue', 'Marill', 'Combee', 'Pichu', 'Tyrogue', 'Marill'))