Test = int(input(""))


for var in range(1, Test+1):
    No_villain = int(input())

    v1 = input()
    Villain = v1.split(" ")
    # print(Villain)
    h1 = input()
    hero = h1.split(" ")
    Villain = list(map(int, Villain))
    Villain.sort(reverse=True)

    hero = list(map(int, hero))
    hero.sort(reverse=True)

    is_win = False
    for var1 in range(0, len(Villain)):
        if Villain[var1] >= hero[var1]:
            is_win = False
            break
        else:
            is_win = True
    if is_win:
        print("WIN")
    else:
        print("LOSE")


# 112 243 512 343 90 478
# 500 789 234 400 452 150