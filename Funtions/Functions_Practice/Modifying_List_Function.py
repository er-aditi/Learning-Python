unprinted_design = ['color', 'size', 'quality']
printed_design = []

while unprinted_design:
    data = unprinted_design.pop()
    print("This is not complete", data)

    printed_design.append(data)


print("\nThe following data: ")
for datas in printed_design:
    print(datas)
