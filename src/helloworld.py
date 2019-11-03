
allsonars = [
             {"Sonar_hull":"548","Sonar Name": "Tally Ho!"},
             {"Sonar_hull":"875","Sonar Name":"Gaijin"},
             {"Sonar_hull":"508","Sonar Name":"Allegedly"},
             {"Sonar_hull":"371", "Sonar Name":"Zataway"}
             ]


def print_allsonarsheadersonly():
    print("length of array1",len(allsonars))

    for x in range(len(allsonars)):
        headersnames = allsonars[x].__getitem__("Sonar_hull")
        print(headersnames)
        #print(allsonars.sonarheader(x))

print_allsonarsheadersonly()






    

