basic_salary = input("Enter Basic salary ")
print(basic_salary)
d = 0.4 * float(basic_salary)
print(d)
h = 0.2 * float(basic_salary)
print(h)
var = float(basic_salary) + float(d) + float(h)
print("Gross Salary is: " + str(var))