l = ["10", "20", "30", "40", "50"]
idx1 = l.index("10")
idx2 = l.index("50")
l[idx1], l[idx2] = l[idx2], l[idx1]

print(l)