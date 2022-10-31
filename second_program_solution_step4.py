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

attribute_list = []

for line in infile:
    #need intermediate list of strings
    attributes = line.split(", ")

    #itterate through list and remove whitespace
    stripped_attributes = [s.strip() for s in attributes]

    #add cleaned up attributes to the attribute list
    attribute_list.append(stripped_attributes)

# ask user how many animals they want to classify

#note input needs to be type cast to int
num_animals = int(input("Please enter number of animals to classify: "))

#check that there are enough input animals
if(num_animals > len(attribute_list) or num_animals < 1):
    print("invalid number of animals")
    exit()

#student test code
print("num_animals =", num_animals)

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
