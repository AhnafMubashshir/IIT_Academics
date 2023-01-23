import csv
import math

import pandas as pd


def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)

        for item in csvreader:
            data.append(item)

    return data[0]

def read_csv_df(file_path):
    df = pd.read_csv(file_path)
    return df

def find_probabilities(value, mean, SD):
    # print(type(mean))
    nominator= pow((value - mean), 2)
    denominator= 2* pow(SD, 2)

    exponential= math.exp(-(nominator/denominator))

    # constant is 1/ root(2*pie)
    constant = 0.3989422804

    probability = (constant * exponential)/SD

    return float(probability)


testingList = []
file2 = open("TestingList.txt", "r")
for i in range(55):
    testingList.append(int(file2.readline()))

# print(testingList)

df = read_csv_df("survival_dataset.csv")

data = read_csv("MeanSD.csv")
Data = [float(x) for x in data]

AgeSurvivedMean = Data[0]
AgeNotSurvivedMean = Data[1]
aNodeSurvivedMean = Data[2]
aNodeNotSurvivedMean = Data[3]
yearSurvivedMean = Data[4]
yearNotSurvivedMean = Data[5]

AgeSurvivedSD = Data[6]
AgeNotSurvivedSD = Data[7]
aNodeSurvivedSD = Data[8]
aNodeNotSurvivedSD = Data[9]
yearSurvivedSD = Data[10]
yearNotSurvivedSD = Data[11]

SP = Data[12]
NSP = Data[13]

TruePositive = 0
TrueNegative = 0
FalsePositive = 0
FalseNegative = 0
totalCount = 0

for i in testingList:
    age = df["Age"].loc[i]
    year = df["Operation Year"].loc[i]
    aNode = df["Auxilary Nodes"].loc[i]


    age = float(age)
    aNode = float(aNode)
    year = float(year)

    AgeSurvivedP = find_probabilities(age, AgeSurvivedMean, AgeSurvivedSD)
    AgeNotSurvivedP = find_probabilities(age, AgeNotSurvivedMean, AgeNotSurvivedSD)
    aNodeSurvivedP = find_probabilities(aNode, aNodeSurvivedMean, aNodeSurvivedSD)
    aNodeNotSurvivedP = find_probabilities(aNode, aNodeNotSurvivedMean, aNodeNotSurvivedSD)
    yearSurvivedP = find_probabilities(year, yearSurvivedMean, yearSurvivedSD)
    yearNotSurvivedP = find_probabilities(year, yearNotSurvivedMean, yearNotSurvivedSD)

    SurvivalP = AgeSurvivedP * aNodeSurvivedP * yearSurvivedP * SP
    NotSurvivalP = AgeNotSurvivedP * aNodeNotSurvivedP * yearNotSurvivedP * NSP

    # print(SurvivalP, NotSurvivalP)

    if SurvivalP >= NotSurvivalP:
        Decision = 1
    else:
        Decision = 2

    if df["Survival Status"].loc[i] == 1:
        if Decision == 1:
            TruePositive += 1
        else:
            FalsePositive += 1
    else:
        if Decision == 1:
            FalseNegative += 1
        else:
            TrueNegative +=1

    totalCount += 1


correctPrediction = TruePositive + TrueNegative
accuracy = (correctPrediction/totalCount) * 100

print("Accuracy: ", accuracy, "%")

file3 = open("accuracy.txt", "a")
file3.write(str(accuracy) + "%\n")

