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
attributes_class = []

for i in range (num_animals):
    attributes = attribute_list[i]

    #if: do if the statement is true
    if(attributes[0] == "antlers" and attributes[1] == "hooves") or (attributes[1] == "antlers" and attributes[0] == "hooves"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = moose")

    #elif <-> "else if": only evaluate the elif statement if the previous if or elif statement is false, do if true
    elif(attributes[0] == "spots" and attributes[1] == "hooves") or (attributes[1] == "spots" and attributes[0] == "hooves"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = cow")
    elif(attributes[0] == "spots" and attributes[1] == "big claws") or (attributes[1] == "spots" and attributes[0] == "big claws"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = lepard")
    elif(attributes[0] == "beak" and attributes[1] == "wings") or (attributes[1] == "beak" and attributes[0] == "wings"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = bird")
    elif(attributes[0] == "beak" and attributes[1] == "big claws") or (attributes[1] == "beak" and attributes[0] == "big claws"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = eagle")
    elif(attributes[0] == "wing" and attributes[1] == "big claws") or (attributes[1] == "wing" and attributes[0] == "big claws"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = eagle")
    elif(attributes[0] == "wing" and attributes[1] == "big ears") or (attributes[1] == "wing" and attributes[0] == "big ears"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = bat")
    elif(attributes[0] == "big ears" and attributes[1] == "big claws") or (attributes[1] == "big ears" and attributes[0] == "big claws"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = dog")
    elif(attributes[0] == "big ears" and attributes[1] == "spots") or (attributes[1] == "big ears" and attributes[0] == "spots"):
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = dog")
    #else: do if all previous statements are false
    else:
        attributes_class.append(attributes[0] + " + " + attributes[1] + " = invalid animal")


# print classifications to the screen
for classification in attributes_class:
    print(classification)

# save classifications to animal_classifications.txt
