# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, 
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

file_1 = open('users.txt', 'r', encoding='utf8') 
key = file_1.readlines()
print(key)
print(file_1.closed)
file_1.close()
print(file_1.closed)
file_2 = open('hobby.txt', 'r', encoding='utf8')
val = file_2.readlines()
print(val)
print(file_2.closed)
file_2.close()
print(file_2.closed)

info = dict(zip(key, val))
print(info)

with open('users_hobby.txt', 'w', encoding='utf8' ) as out:
    for key, val in info.items():
        out.write('{}: {}'.format(key, val))


