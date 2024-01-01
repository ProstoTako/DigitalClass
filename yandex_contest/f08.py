words = input().split(", ")
count_word = dict()
for word in words:
    if word != '':
        count_word[word.strip()] = count_word.get(word.strip(), 0) + 1
l = ((count, word) for word, count in count_word.items())
for count, word in sorted(l, reverse=True)[:3]:
    print(f"{word}: {count}")