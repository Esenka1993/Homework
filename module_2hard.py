import random
set1 = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
pillar1 = list(set1)
d = int(random.choice(pillar1))
print(d)
unique_pairs = set()
for i in range(1, 21):
    for j in range(i+1, 21):
        kr = i + j
        i != d
        if d % kr == 0 and i != j:
            result = str(i) + str(j)
            unique_pairs.add(result)
print(*sorted(unique_pairs))

