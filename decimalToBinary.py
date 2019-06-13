#This is a python program that converts decimal to binary
#wrote by Ruotian Liu

check = 1
print("Decimal - Binary converter: ")

while check == 1:
    decimal = input("Enter a decimal number: ")
    try:
        val = int(decimal)
        if val >= 0:
            check = -1
    except ValueError:
        print("please enter a decimal number")

print("Decimal: " + str(decimal))
a = int(decimal)
flag = 1
count = []

while flag == 1:
    temp = a%2
    count.append(int(temp))
    #print(temp)
    a = a - temp
    if a == 0:
        break
    else:
        a = a/2

s = [str(i) for i in count]
binary = "".join(s)

print("Binary: " + binary[::-1])