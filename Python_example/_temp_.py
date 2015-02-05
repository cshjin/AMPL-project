cond = []
clu_cond = []
with open("conditions.txt") as infile:
    for i in infile:
        cond.append(int(i))
for i in cond:
    if i in [15, 23, 38, 39]:
        clu_cond.append(1)
    elif i in [10, 24, 29, 40, 42]:
        clu_cond.append(2)
    elif i in [1, 13, 21, 22, 25]:
        clu_cond.append(3)
    elif i in [3, 6, 26]:
        clu_cond.append(4)
    elif i in [2, 28, 33, 35]:
        clu_cond.append(5)
    elif i in [4, 5, 7, 9, 19, 20, 27, 30, 31, 41]:
        clu_cond.append(6)
    elif i in [8, 11, 16, 17, 18, 32, 34]:
        clu_cond.append(7)
    elif i in [12, 14, 36, 37]:
        clu_cond.append(8)
    # elif i in [16,17,18,19,20,21]:
    # 	clu_cond.append(8)
    # elif i in [16,17,18,19,20,21]:
    # 	clu_cond.append(8)
print clu_cond[100:200]
with open("cluster_condition_2.txt", "w") as outfile:
    for i in clu_cond:
        outfile.write(str(i) + "\n")
print len(cond)
