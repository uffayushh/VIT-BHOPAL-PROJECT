import string
import random

t1 = list(string.ascii_lowercase)
t2 = list(string.ascii_uppercase)
t3 = list(string.digits)
t4 = list(string.punctuation)

user_input = input("How many characters do you want in your password? ")

while True:
    try:

        characters_number = int(user_input)

        if characters_number < 8:

            print("Your number should be at least 8.")

            user_input = input("Please, Enter your number again: ")

        else:

            break

    except:

        print("Please, Enter numbers only.")

        user_input = input("How many characters do you want in your password? ")

random.shuffle(t1)
random.shuffle(t2)
random.shuffle(t3)
random.shuffle(t4)

p1 = round(characters_number * (30/100))
p2 = round(characters_number * (20/100))


result = []

for x in range(p1):

    result.append(t1[x])
    result.append(t2[x])

for x in range(p2):

    result.append(t3[x])
    result.append(t4[x])


# shuffle the result to make it an even harder password
random.shuffle(result)

Pass = "".join(result)
print("Strong Password: ", Pass)
	