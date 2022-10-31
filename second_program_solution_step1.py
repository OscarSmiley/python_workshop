import random

attributes = ["spots", "antlers", "hooves", "big claws", "wings", "beak", "big ears"]

f = open("animal_attributes.txt", "w")

for i in range (20):
    f.write(attributes[random.randint(0,6)] + ", " + attributes[random.randint(0,6)] + "\n")

f.close()

# ******* student code here ******
# read animal_attributes.txt into memory

infile = open("animal_attributes.txt", "r")

outfile = open("animal_classifications.txt", "w")

for line in infile:
    #place holder print for student to check their work
    print(line)

# ask user how many animals they want to classify

# classify:
# antlers + hooves -> moose
# spots + hooves -> cow
# spots + big claws -> lepard
# beak + wings -> bird
# beak + big claws -> eagle
# wings + big claws -> eagle
# wings + big ears -> bat
# big ears + big claws -> dog
# big ears + spots -> dalmation
# ANY OTHER COMBINATION -> invalid animal

# print classifications to the screen

# save classifications to animal_classifications.txt
