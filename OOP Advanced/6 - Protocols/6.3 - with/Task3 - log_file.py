

# Сравнение что входная дата есть в файле, если есть то записываем в output и создаем log_file_date


def log_for(logfile, datetime):
    
    with open(logfile, 'r', encoding='UTF-8') as input_file, open(f'log_for_{datetime}.txt', 'w', encoding="UTF-8") as output_file:
            for line in input_file:
                if datetime in line:
                    output_file.write(line)




# TEST_1:
with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())
print()
# TEST_2:
data = '''2022-01-07 INFO: User is here
2022-01-15 INFO: Username is True
2022-01-29 INFO: Engine started
2022-01-02 INFO: Hello world
2022-01-03 INFO: Engine started
2022-01-11 ERROR: File not found
2022-01-31 ERROR: Shaders not supported
2022-01-07 ERROR: User is nub
2022-01-11 ERROR: CPU not found
2022-01-07 INFO: Patrick
2022-01-25 INFO: Engine started
2022-01-15 INFO: I`am glad
2022-01-07 ERROR: File not found
2022-01-07 INFO: Start Beegeek OOP Course
2022-01-17 INFO: It`s amazing!
2022-01-25 ERROR: File not found
2022-01-06 INFO: Engine started
2022-01-25 INFO: Algorithms
2022-01-09 ERROR: Shaders not supported
2022-01-07 INFO: Goodbye'''

with open('log.txt', 'w', encoding='utf-8') as file:
    print(data, file=file)

log_for('log.txt', '2022-01-07')

with open('log_for_2022-01-07.txt', encoding='utf-8') as file:
    print(file.read())