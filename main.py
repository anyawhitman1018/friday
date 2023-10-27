string = "I am happy that it is friday"

#This is my first for loop
for i in range(0, len(string), 4):
    print(string[i], end = ":")

#I am going to commit the first loop now
def making_a_list():
    for i in range(0, len(string), 4):
        output = []
        output.append(string[i])
    return output 