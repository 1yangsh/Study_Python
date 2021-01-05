i = 1
cnt = 1

while(i < 7):
    print ("# ", end="")
    for j in range(i, 9):
        print(" ", end="")

    for k in range(0, cnt):
        print("*", end="")
    cnt += 2
    print("")
    i += 1