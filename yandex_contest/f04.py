string = input()
sub_string = input()
sub_string = sub_string.lower()
words_in_string = string.split()

for word in words_in_string:
    if word.lower().find(sub_string) != -1:
        print(word)
