L = [8, 24, 48, 2, 16]
count = 0
for i in L:
    if i % 3 == 0:
        count += 1
        print("Le nombre de multiples de 3 dans la liste est :", count)