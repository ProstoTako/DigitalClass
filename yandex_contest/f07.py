words = input().lower().split(", ")
print(*sorted(set(words)), sep=", ")