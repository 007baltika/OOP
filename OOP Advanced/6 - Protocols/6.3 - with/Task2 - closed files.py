# Реализуйте функцию non_closed_files() , которая принимает один аргумент:
# • files — список файловых объектов
# Функция должна возвращать список, элементами которого являются открытые
# файловые объекты из списка files .

def non_closed_files(files):
    spisok = []
    for file in files:
        if file.closed:
            continue
        else: spisok.append(file)
    return spisok           
             
             
#НЕ ЗАПУСКАТЬ! ГЕНЕРИРУЕТ КУЧУ ТЕКСТОВИКОВ!             
                
                
# TEST_1:
with (
    open('file1.txt', 'w', encoding='utf-8') as file1,
    open('file2.txt', 'w', encoding='utf-8') as file2,
    open('file3.txt', 'w', encoding='utf-8') as file3
):
    file1.write('i am the first file')
    file2.write('i am the second file')
    file3.write('i am the third file')

file1 = open('file1.txt', encoding='utf-8')
file3 = open('file3.txt', encoding='utf-8')


for file in non_closed_files([file1, file2, file3]):
    print(file.read())
print()
# TEST_2:
files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt',
         'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt', 'file15.txt', 'file16.txt',
         'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt']

contents = ['Among agency health total.', 'Skin mind story market.', 'Order clearly institution dark.',
            'Bed best personal enough product.', 'Tree key language level.',
            'Standard any simple national play whether whatever.', 'Fine tree kind last interesting any.',
            'Population less staff school.', 'Ball light hospital work.', 'Blue put life.',
            'Site difficult argue all article civil.', 'Which positive can speak.',
            'Know general great why early choice against.', 'Become million establish difference left.',
            'Community entire bit fund population indeed.', 'Market authority debate decision.',
            'Answer player cup agency later gun power blue.', 'Building card answer need a serve partner.',
            'Tend suddenly skill over alone enough television.', 'Minute cover realize before report.']


for file, content in zip(files, contents):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

array = [open(f, encoding='utf-8') for f in files]
count = 0
for f in array:
    if count % 2 == 0:
        f.close()
    count += 1


for file in non_closed_files(array):
    print(file.read())              