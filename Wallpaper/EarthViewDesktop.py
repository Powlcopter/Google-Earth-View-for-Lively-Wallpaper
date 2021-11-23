from os.path import exists
import http.client as http
from urllib.parse import urlparse

def strip(string): # strip string of whitespace and make it lowercase
    return string.replace(" ", "").lower()


def ynCheck(question): # simple yes/no check
    answer = strip(input(question + " (y/n):\n"))
    if(answer== "y" or answer == "yes"):
        return True
    elif(answer == "n" or answer == "no"):
        return False
    else:
        input("\nInvalid input! Press Enter to exit\n")
        exit(1)

def checkUrl(url): # check if url is valid or a 404
    p = urlparse(url)
    conn = http.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400


def getLastID(): # get last ID in file
    file = open(filePath, "r")
    empty = True
    for line in file: # get last line
        empty = False
    file.close()
    if empty:
        return 0
    return int(line)


def listGen(start, end): # generate list of IDs
    j = 0
    IDs = ""
    total = end-start
    if total < 0:
        print("\nError: End point (", str(end), ") must be greater than start point (", str(start), "). Press Enter to exit\n")
        exit(1)
    if total > 1000:
        if not ynCheck("You are about to check for " + str(total) + " IDs. This may take a long time. Do you want to continue?"):
            input("\nCancelled. Press Enter to exit\n")
            exit(1)
    print("Generating list of Image IDs, please wait...")
    for i in range(start, end):
        if checkUrl("https://www.gstatic.com/prettyearth/assets/full/" + str(i) +  ".jpg"):
            IDs = IDs + str(i) + "\n"
            j+=1
        print("Currently at", i-start+1, "out of", str(total) +  ", found", j, "valid IDs so far", end='\r')
    print()
    print("Found", j, "IDs")
    return IDs


def fullListGen(start, end): # completely regenerate list of IDs
    file = open(filePath, "w")
    file.write(listGen(start, end))
    print("Successfully wrote IDs to file")
    file.close()


def extendList(end): # extend list of IDs, starting at the current last ID
    file = open(filePath, "r")
    start = getLastID() + 1
    file = open(filePath, "a")
    file.write(listGen(start, end))
    print("Successfully wrote IDs to file")
    file.close()


def main():
    global filePath
    start = 1000
    end = 15000
    print("\nWelcome to the Google Earth View ID generator!\nThis script will generate a list of valid image IDs by testing if the corresponding image exists on Googles's servers.\nThis will most likely take a while.\nRunning this script is NOT NECESSARY. It only makes sure you get all the newest images.\nYou should probably make a copy of the imageIDs.txt before you use this just in case.\n")
    """
    if ynCheck("Do you want to set a custom file path? (ONLY RECCOMENDED FOR TESTING PURPOSES"):
        filePath = input("Enter file path (relative to this script, including file name and extension): ")
        if not exists(filePath):
            if ynCheck("File does not exist. Do you want to create it?"):
                fileCreation = open(filePath, 'x')
                fileCreation.close()
            else:
                print("\nCancelled. Press Enter to exit\n")
                exit(0)
    """
    if not exists(filePath):
        if ynCheck("ImageIDs.txt not found. Do you want to create it?"):
            fileCreation = open(filePath, 'x')
            fileCreation.close()
        else:
            print("\nCancelled. Press Enter to exit\n")
            exit(1)
    genType = strip(input("Do you want to generate a full list of IDs or extend an existing list? (f/e):\n"))
    lastID = getLastID()
    if genType == "f":
        print("\nThis will completely regenerate the ID list from scratch.\n")
        startInput = strip(input("Enter starting ID (leave blank for default = 1000):\n"))
        if startInput == "":
            start = 1000
        else:
            start = int(startInput)
        endInput = strip(input("Enter ending ID (leave blank for default = 15000):\n"))
        if endInput == "":
            end = 15000
        else:
            end = int(endInput)
        fullListGen(start, end)
    elif genType == "e":
        print("\nThis will extend the ID list by adding the new IDs, starting from the last ID in the file:", str(lastID) + ".\n")
        endInput = strip(input("Enter ending ID (leave blank for default = 15000):\n"))
        if endInput == "":
            end = 15000
        else:
            end = int(endInput)
        extendList(end)
    else:
        print("\nInvalid input. Press Enter to exit\n")
        exit(1)
    input("\nDone! Press Enter to exit\n")


filePath = "imageIDs.txt"
main()