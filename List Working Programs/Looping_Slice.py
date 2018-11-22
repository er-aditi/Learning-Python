players = ['john', 'Ben', 'tom', 'carry']
for player in players[:3]:
    print(player.title())

scores = [1, 20, 50, 60, 55, 63, 86]
scores.sort()
print(scores)

for score in scores[-3:]:
    print(score)

scores_1 = list(scores[-3:])
print(scores_1)

scores_1.sort(reverse=True)
print(scores_1)

bests = list(players[:3])
print(bests)

print("\n-----------------------------------------\n")

for index in range(0, 3):
    if index == 0:
        sign = "st"
    elif index == 1:
        sign = "nd"
    elif index == 2:
        sign = "rd"
    else:
        sign = 'th'

    print(str(bests[index].title()) + " is the " + str(index + 1) + sign + " player of chess. He scored " + str(
        scores_1[index]) + ".")
# print(str(bests[index].title()) + " is the first player of chess. He scored " + str(scores_1[index]) + ".")
# for score_1 in scores_1:
# print(str(bests) + " is the first player of chess. He scored " + str(scores_1))
# print(str(bests) + " is the Second player of chess. He scored " + str(scores_1))
# print(str(bests) + " is the Third player of chess. He scored " + str(scores_1))


