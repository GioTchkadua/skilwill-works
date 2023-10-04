words = []
for i in range(5):
    x = input(f"Please enter word {i + 1}: ")
    words.append(x)


print(len(max(words, key=len)))
