import string
import random

# print(''.join(random.choice(string.ascii_uppercase) for i in range(12)))
import random
import string
from random import randint

def random_string_loop():
    with open("exercise_five.dat", "r+") as f:

        for num in range(0, 10):  # Represents number of strings printed

            random_integer = randint(0, 101)
            random_string = ''.join([random.choice(string.ascii_letters) for i in range(0, random_integer)])  # Represents number
            # of char within string
            # with open("exercise_five.dat", "r+") as f:
            #     f.write(random_string)

            print random_string

            # count characters
            letters_seen = {}
            for char in random_string:
                if char in letters_seen:
                    # increment
                    letters_seen[char] += 1
                    #letters_seen[char] = letters_seen[char] + 1
                else:
                    # create new key
                    letters_seen[char] = 1

            # print count result
            final_print = ""
            for k,v in letters_seen.items():
                final_print += k + " ==> " + str(v) + " "

            print final_print

            f.write(random_string + "\n")

#random_string_loop()


with open("war_and_peace.txt", "r") as f:
    txt = f.read()

exclude = set(string.punctuation)
clean_text = ''.join(char for char in txt if char not in exclude)

txt_list = clean_text.replace("\n", " ").lower().split(" ")

war_and_peace = {}
for word in txt_list:
    #print "word?: " + word
    if word in war_and_peace:
        #increment
        war_and_peace[word] += 1
        #war_and_peace[word] = war_and_peace [word] + 1

    else:
        # create new key
        war_and_peace[word] = 1


f = (line for line in open("war_and_peace.txt").xreadlines())  # how much is loaded in memory?

f.next()



print war_and_peace