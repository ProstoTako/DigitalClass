string = input().lower()
count_the_most_popular_words = 3

list_string = string.split(', ')
list_string.sort()

dictionary = dict()
index = 0
while index != len(list_string):
    new_word = list_string[index]
    count = list_string.count(new_word)
    dictionary[new_word] = count
    index += count

list_count = list(dictionary.values())
list_count.sort(reverse=True)
list_the_needed_count = list_count[:count_the_most_popular_words]

for count in list_the_needed_count:
    for word in dictionary:
        if count == dictionary[word]:
            print(f'{word}: {count}')
            del dictionary[word]
            break
