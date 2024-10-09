def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i:j + 1]

for a in all_variants('abc'):
    print(a)