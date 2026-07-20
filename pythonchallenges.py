#guessing game

secret_word = "alice"


while True:
    guess = input("please enter guess: ")
    if secret_word == guess:
        break
    print("you have guess incorrectly. try again")


print("done")


#multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()

# or
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")






## prime checker

x = int(input("please enter the number you want to check: "))
if x <=1:
    print(f"{x} is a prime number")
else:
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{x} is a prime number')
    else:
        print(f'{x} is not a prime number')



# #password validator
password = input("please enter a password that is at least 4 characters long and contains a number")

if len(password) >= 4:
    if any(char.isdigit() for char in password):
        print("valid ")
    else:
        print("please include a number in your password")
else:
    print("invalid")
# calculate averages
def calc_avg(x,y):
    return (x+y)/2



# find maximum 

def fin_max(x,y):
    if x>y:
        return x
    else:
        return y
    

# clear text


def clear_text(text):
    return text.strip().lower().replace(" ", "")


# count vowels


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count






def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for letter in text:
        if letter in vowels:
            count +=1
    return count














# check palindrome: if not say not palindrome, if so say it's palindrome

def check_palindrome(word):
    word = clear_text(word)
    if word == word[::-1]:
        return True
    else:
        return False





def check_negative(num):
    if num > 0:
        return False
    else:
        return True


print(check_negative(-5))

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
