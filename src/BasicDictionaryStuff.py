
allsonars = [
             {"Sonar_hull":"548","Sonar Name": "Tally Ho!","Owner":"Brown"},
             {"Sonar_hull":"875","Sonar Name":"Gaijin","Owner":"Luke"},
             {"Sonar_hull":"508","Sonar Name":"Allegedly","Owner":"Bergam"},
             {"Sonar_hull":"371", "Sonar Name":"Zataway", "Owner":"Rainaldi"}
             ]


def print_allsonarsheadersonly():
    print("length of array1",len(allsonars))

    for x in range(len(allsonars)):
        headersnames = allsonars[x].__getitem__("Owner")
        print(headersnames)

def print_AllDicts():
    for x in range(len(allsonars)):
        print(allsonars[x])

def print_ownerbyHullNumber(HullNumber):
    #print("calling owner by hullnumber")    #ghetto debugging
    for x in range (len(allsonars)):
        DictHullNumber = allsonars[x].__getitem__("Sonar_hull")
        #print(HullNumber,DictHullNumber)   # ghetto debugging

        if HullNumber == allsonars[x].__getitem__("Sonar_hull"):
            print("Owner of Hull Number",HullNumber, "Is:", allsonars[x].__getitem__("Owner"))
            return

    print("no owner for this hull:",HullNumber)

def append_NewSonar(HullNumber,Boatname,OwnerName):
    NewSonar =  {"Sonar_hull": HullNumber,"Sonar Name": Boatname,"Owner":OwnerName}
    allsonars.append(NewSonar)

#sample for testing *args
def var_argsFunction(*args):
    print(args)


#sample for **kwargs
def var_kwargsFunction(**kwargs):
    print(kwargs["name"],kwargs["bool"])

def AddSonarwithInput():
    newSonarHullNumber = input("enter new Sonar Hull Number:")
    newSonarBoatName = input("enter new Sonar name:")
    newSonarOwner = input("enter new Sonar owner:")
    #print(newSonarBoatName,newSonarHullNumber,newSonarOwner)
    NewSonar = {"Sonar_hull": newSonarHullNumber, "Sonar Name": newSonarBoatName, "Owner": newSonarOwner}
    allsonars.append(NewSonar)

#print_allsonarsheadersonly()
#print_ownerbyHullNumber("215")
#append_NewSonar("4","Hollinger")
#print_AllDicts()
#append_NewSonar("004","Forte","Hollinger")
#print_AllDicts()
#var_argsFunction("good","job","on","MTS")
#var_kwargsFunction(name = "good job", description='kwargs',bool = True)

#add new sonar hull number, name and owner with input function and then verify print
AddSonarwithInput()
print_AllDicts()






    

