import json

filePath = "imageIDs.txt"
outputPath = "imageIDs.json"

txtFile = open(filePath, "r")
jsonFile = open(outputPath, "w")
idArray = []
jsonDict = {}
jsonOut = ""


i = 0
for line in txtFile:
    idArray.append(line.strip())
    i+=1
    
jsonDict["amountOfIDs"] = i
jsonDict["imageIDs"] = idArray

jsonOut = json.dumps(jsonDict)

jsonFile.write(jsonOut)

print(jsonDict)

txtFile.close()
jsonFile.close()