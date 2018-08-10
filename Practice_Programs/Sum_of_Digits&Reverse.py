digit = input("Enter 5 digit Numbers: ")
print(int(digit))
num_5 = int(digit) % 10
num_a = int(digit)/10
num_4 = int(num_a) % 10
num_b = int(num_a)/10
num_3 = int(num_b) % 10
num_c = int(num_b)/10
num_2 = int(num_c) % 10
num_1 = int(num_c) // 10
print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)

sum_1 = num_1+num_2+num_3+num_4+num_5
print("Sum of 5 digit is = " + str(sum_1))

# Reverse
rev = num_5*10000 + num_4*1000 + num_3*100 + num_2*10 + num_1
print(rev)