# count of odd and even numbers
odd_num = 0
even_num = 0
num = int(input("Enter a number or type 0 to stop: "))

while num!=0:
    if num%2 == 0:
        even_num += 1
    else:
        odd_num += 1
    num = int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count is ", odd_num)
print("Even numbers count is ", even_num)
