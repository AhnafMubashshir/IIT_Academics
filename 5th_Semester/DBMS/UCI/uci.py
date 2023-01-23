import csv
import random

import pandas as pd
import math

from Tools.scripts.dutree import display


def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def write_csv(filePath, data):
    file = open(filePath, 'w')

    writer = csv.writer(file)
    writer.writerow(data)

    file.close()
def calculateSD(df, mean):

    sum = 0
    for item in df:
        sum += pow((item-mean), 2)

    calculatedSD = sum/(len(df)-1)

    return math.sqrt(calculatedSD)



forTesting = [False]*306

file = open("TestingList.txt", "w")
count = 0
while count < 62:
    rnd = random.randint(1,305)
    if forTesting[rnd] == False:
        forTesting[rnd] = True
        count  += 1


for i in range(306):
    if forTesting[i]:
        file.write(str(i) + "\n")


Data = read_csv("survival_dataset.csv")


data = pd.DataFrame(index= ["Age","Operation Year" ,"Auxilary Nodes", "Survival Status"])

for i in range(306):
    if forTesting[i]==False:
        # print(Data.loc[i])
        data = data.append(Data.loc[i])

data = data.dropna()
data = data.reset_index()
tot_data = len(data["Survival Status"])


SurvivalStat = data["Survival Status"].value_counts()
SurvivalStat = SurvivalStat/tot_data

SurvivalP = SurvivalStat[1]
NotSurvivalP = SurvivalStat[2]

# print(SurvivalP, NotSurvivalP)

gk = data.groupby("Survival Status")

AgeSurvived = gk["Age"].get_group(1)
AgeNotSurvived = gk["Age"].get_group(2)

aNodeSurvived = gk["Auxilary Nodes"].get_group(1)
aNodeNotSurvived = gk["Auxilary Nodes"].get_group(2)

yearSurvived = gk["Operation Year"].get_group(1)
yearNotSurvived = gk["Operation Year"].get_group(2)

totAgeSurvived = AgeSurvived.sum()
totAgeNotSurvived = AgeNotSurvived.sum()
totaNodeSurvived = aNodeNotSurvived.sum()
totaNodeNotSurvived = aNodeNotSurvived.sum()
totYearSurvived = yearSurvived.sum()
totYearNotSurvived = yearNotSurvived.sum()

AgeSurvivedMean = totAgeSurvived/len(AgeSurvived)
AgeNotSurvivedMean = totAgeNotSurvived/len(AgeNotSurvived)
aNodeSurvivedMean = totaNodeSurvived/len(aNodeSurvived)
aNodeNotSurvivedMean = totaNodeNotSurvived/len(aNodeNotSurvived)
yearSurvivedMean = totYearSurvived/len(yearSurvived)
yearNotSurvivedMean = totYearNotSurvived/len(yearNotSurvived)

AgeSurvivedSD = calculateSD(AgeSurvived, AgeSurvivedMean)
AgeNotSurvivedSD = calculateSD(AgeNotSurvived, AgeSurvivedMean)
aNodeSurvivedSD = calculateSD(aNodeSurvived, aNodeSurvivedMean)
aNodeNotSurvivedSD = calculateSD(aNodeNotSurvived, aNodeNotSurvivedMean)
yearSurvivedSD = calculateSD(yearSurvived, yearSurvivedMean)
yearNotSurvivedSD = calculateSD(yearNotSurvived, yearNotSurvivedMean)

row = [AgeSurvivedMean, AgeNotSurvivedMean, aNodeSurvivedMean, aNodeNotSurvivedMean, yearSurvivedMean, yearNotSurvivedMean,
       AgeSurvivedSD, AgeNotSurvivedSD, aNodeSurvivedSD, aNodeNotSurvivedSD, yearSurvivedSD, yearNotSurvivedSD,
       SurvivalP, NotSurvivalP]


write_csv("MeanSD.csv", row)

print("\nTraining Done")