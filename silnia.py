def silnia(x):
    if x < 1:
        print("1")
    else:
        a=1
        for b in range(1,x+1):
            a *= b
        print(a)
silnia(int(input("wpisz silnie: ")))
            