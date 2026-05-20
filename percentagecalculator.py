# take marks as input from user

print("Enter the marks entered in 5 subjects:")

math = int(input("maths :"))

english = int(input("english :"))

science = int(input("science :"))

hindi = int(input("hindi :"))

IT = int(input("IT :"))

# Let's calculate the percentage of the marks

sum = math+english+science+hindi+IT

print("the sum of math,english,science,hindi & IT is:", sum)

perc = (sum/500)*100

print(end="Percentage Mark = ")

print(perc)