import json
import os
print('Здравствуйте!')
print('Я готов становиться крутой AI')
print('end - закончить обучение.')
print('top - топ самых весомых слов.')
print()

if os.path.exists('know.json'):
    with open('know.json', 'r', encoding='utf-8') as f:
        know = json.load(f)
else:
    know = {}

def show_top():
    items = list(know.items())
    items.sort(key=lambda x: x[1])
    print(">>>")
    print("-- TOP-5 грустных слов --")
    for i in range(5):
        if i < len(items):
            word, val = items[i]
            print(f"{i+1}. {word}: {val:.2f}")
    print('''
          ''')
    print("-- TOP-5 весёлых слов --")
    for i, (word,val) in enumerate(items[-5:][::-1]):
        print(f"{i+1}. {word}: {val:.2f}")
    print(">>>")
            
while True:
    data = input('Введите текст: ').lower().split()
    if 'end' in data: break
    if 'top' in data:
        show_top()
        continue

    score = 0
    for word in data:
        score += know.get(word, 0)
    print(f'Мой ответ : {score}')

    real = int(input('А сколько должно быть? : '))
    error = real - score
    for word in data:
        know[word] = know.get(word, 0) + (error * 0.1)

    with open('know.json', 'w', encoding='utf-8') as f:
        json.dump(know, f, ensure_ascii=False, indent=4)
    print()
    print('Окей, я понял.')
    print('Весы в JSON успешно обновлены!')
    print()
