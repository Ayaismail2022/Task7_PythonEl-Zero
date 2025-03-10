"""
Task 7
"""
print(bool(242))
print(bool("Aya"))
print(bool(24.098))
print(bool(True))

print("---------------------------")

print(bool(0))
print(bool(False))
print(bool(""))
print(bool([]))

print("---------------------------")
# لازم يتكتب في سطر واحد

html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript > 50)

print("------------------------------")

num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("------------------------------")

result = num_one + num_two
print(result) 

power = result ** 3
print(power) 

modelus = power % 26000
print(modelus) 

division = modelus / 5
print(float(division))

string_result = str(division)
print(type(string_result))  


