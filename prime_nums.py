#Write your code below this line 👇
def prime_checker(number):
    if number%2==0:
        if number!=2:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    elif number%3==0:
        if number!=3:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    elif number%5==0:
        if number!=5:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    elif number%7==0:
        if number!=7:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    elif number%11==0:
        if number!=11:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    else:
        print("It's a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
