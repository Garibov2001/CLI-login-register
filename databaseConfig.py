import json

def GetDataFromJson(fileName):
    dataList = []
    with open(fileName, 'r') as outfile:
        dataList = json.load(outfile)
    return dataList


def SetDataToJson(fileName, dataList):
    with open(fileName, "w") as connect:
        json.dump(dataList, connect)  
