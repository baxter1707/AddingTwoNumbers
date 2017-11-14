number1 = raw_input("What is your age?")
number2 = raw_input("What is your favorite number?")

i = int(number1)
x = int(number2)
sum = float(i) + float(x)

#print(sum)

message = "The combined number is {0}.".format(sum)

print(message)
