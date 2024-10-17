from collections import defaultdict

word_count = defaultdict(int)

tekst = "python jest super, python jest doskonały, python jest liderem"

#zliczanie wystąpień słów
for word in tekst.split():
    word_count[word] += 1

#wyniki
for word,count in word_count.items():
    print(f"{word}: {count}")
