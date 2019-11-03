from time import time_ns
from time import sleep

SonarNames = ["Tally Ho!","Surly Angel","Zataway","Gaijin"]

def  SortSonarNames(list):
    list.sort()

def  SortSonarNamesReverse(list):
    list.sort(reverse=True)


def  EpochTime():
    return time_ns()



def EpochTimeDiff(begintime):
    endtime = time_ns()
    return (endtime - begintime)


print("unsorted sonar names", SonarNames)

SortSonarNames(SonarNames)

epochnanosecs = EpochTime()

print("Epoch Nanoseconds",  epochnanosecs)

print("Sorted Sonar Names", SonarNames)

SortSonarNamesReverse(SonarNames)
sleep(3)
timedifference= EpochTimeDiff(epochnanosecs)
print("time difference:", timedifference)

print("Sorted Sonar Names in Reverse", SonarNames)

