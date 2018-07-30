even_numbers = list(range(2, 21, 2))
print(even_numbers)

for even_number in even_numbers:
    print("These are the even values: ".title() + str(even_number))

print("\n")

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

for odd_number in odd_numbers:
    print("These are the odd Values: ".title().strip() + str(odd_number))
    
print("Well Done!")    
