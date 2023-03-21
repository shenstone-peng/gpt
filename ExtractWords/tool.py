with open('file.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for line in lines:
        pairs = line.split(';')
        for pair in pairs:
            if '@' in pair:
                word = pair.split('@')[1]
                words.append(word)

with open('words.txt', 'w') as f:
    f.write(','.join(words))