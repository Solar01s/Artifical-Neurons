import json
import os

try:

    def markov_learn(learning_words):
        words = learning_words
        for i in range(len(words) - 1):
            current = words[i].replace('.', '').replace(',', '')
            next_word = words[i+1].replace('.', '').replace(',', '')
            if current not in links:
                links[current] = {}
                links[current][next_word] = links[current].get(next_word, 0) + 1
            
            with open('links.json', 'w', encoding='utf-8') as f:
                json.dump(links, f, ensure_ascii=False, indent=4)

    def go():
        print()
        print('Опа-на!')
        print()
        word = input('Введите слово: ')
        sentence = [word]
        try:
            for i in range(5):
                if word in links:
                    options = links[word]
                    next_word = max(options, key=options.get)
                    sentence.append(next_word)
                    word = next_word
            else:
                print(f'Слово "{word}" - тупик. Цепочка прервана')
        except Exception as e:
            print(f'Произошла ошибка данных: {e} #_#')
        print('Предложение: ',' '.join(sentence), '.')

    print("Привет! - я учусь запоминать предложения.")
    print("end - закончить обучение.")
    print("go - проверить связи, введя слово")
    print()

    DIR = os.path.dirname(os.path.abspath(__file__))
    links_path = os.path.join(DIR, 'links.json')
    print(links_path)
    if os.path.exists(links_path):
            with open(links_path, 'r', encoding='utf-8') as f:
                links = json.load(f)
    else:
        with open(links_path, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
            print("UUU")
        with open(links_path, 'r', encoding='utf-8') as f:
            links = json.load(f)

    while True:
        phrase = input('Введите фразу: ')
        words = phrase.replace('.', '').replace(',', '')
        words = words.lower().split()
        
        if 'end' in words: break
        if 'go' in words: go()

        for i in range(len(words) - 1):
            current = words[i]
            next_word = words[i+1]
            if current not in links:
                links[current] = {}
                links[current][next_word] = links[current].get(next_word, 0) + 1
                
        with open(links_path, 'w', encoding='utf-8') as f:
            json.dump(links, f, ensure_ascii=False, indent=4)
                
        print("Я запомнил текст!")
        
except Exception as e:
    print(f'Критическая ошибка prediction_nueron: {e}')
