L = ["10", "20", "30", "40", "50"]
print (L[1])
def modifier_liste(L):
    L[3] = L[2] + L[4]
    modifier_liste(L)
print(L[3])
print (L[-1])