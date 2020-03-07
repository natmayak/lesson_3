# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content.split(" ")))

with open('referat.txt', 'w', encoding='utf-8') as f:
    f.write(content.replace('.', '!'))
    print(content)

with open('referat_modified.txt', 'w', encoding='utf-8') as f:
    f.write(content)



