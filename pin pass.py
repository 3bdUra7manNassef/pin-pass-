import string
import random
number =list(string.digits)
while True:
    try:
        numbers_pasword = input("enter number to pasword:")
        numbers_pasword = int(numbers_pasword)
        if numbers_pasword < 4:
            print("you nead more number")
            numbers_pasword = input("enter number to pasword:")
        else:
            numbers_pasword =int (input("enter number to pasword:"))
            random.shuffle(number)
            password = []
            Prospect = round(numbers_pasword*(100/100))
            for i in range(Prospect):
                password.append(number[i])
            password="".join(password[0:])
            print("your password----> " + password)
    except:
        print("error please try agin")
