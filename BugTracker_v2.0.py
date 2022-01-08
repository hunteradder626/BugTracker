import os
from datetime import datetime

#create a new request
def New_Request():
    bugSubject = input("What is the nature of the bug you have found? ")
    bugBody = input("What can you tell me about the bug? ")
    while bugBody == "":
        bugBody = input("What can you tell me about the bug? ")

    bugReport = "Title:     " + bugSubject + "\n\n" + "Body:    " + bugBody
    
    #go into the request folder
    #highest number from the files stored?
    cwd = os.getcwd()
    path = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Requests/"
    os.chdir(path)
    
    #get highest number in incomplete bug list
    listOfFileNames = [0,]
    for eachFile in os.listdir(path):
        if eachFile != ".DS_Store":
            fileName = []
            fileName = eachFile.split()
            # print(fileName)
            listOfFileNames.append(int(fileName[0]))
            
    #get highest number in completed bug list
    listOfCompletedFileNames = [0,]
    completedPath = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Completed/"
    for everyFile in os.listdir(completedPath):
        if everyFile != ".DS_Store":
            completedFileName = []
            completedFileName = everyFile.split()
            # print(completedFileName)
            listOfCompletedFileNames.append(int(completedFileName[0]))

    if listOfFileNames == [0] and listOfCompletedFileNames == [0]:
        bugNumber = 1
    else:    
        # if listOfFileNames != []:
        listOfFileNames.sort()
        # print(listOfFileNames)
        listOfCompletedFileNames.sort()
        # print(listOfCompletedFileNames) 
        biggestListOfFileNames = listOfFileNames[-1]
        biggestListOfCompletedFileNames = listOfCompletedFileNames[-1]
        if biggestListOfFileNames > biggestListOfCompletedFileNames:    
            bugNumber = biggestListOfFileNames + 1
            # print(biggestListOfFileNames + 1)
        if biggestListOfCompletedFileNames > biggestListOfFileNames:
            bugNumber = biggestListOfCompletedFileNames + 1
            # print(biggestListOfCompletedFileNames + 1)
        if biggestListOfCompletedFileNames == biggestListOfFileNames:
            bugNumber = biggestListOfFileNames + 1         
        # else:
        #     bugNumber = listOfCompletedFileNames[-1]
    # #store the request
    request = str(bugNumber) + " " + bugSubject + ".txt"

    with open (request, 'w') as f:
        f.write(bugReport)    
    
    return bugSubject,bugReport,bugNumber

# bugSubject, bugReport, bugNumber = New_Request()

#ammend request
def AmmendRequest():
    cwd = os.getcwd()
    path = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Requests/"
    listOfExistingBugs = []
    
    print("All files:")
    for everyFile in os.listdir(path):
        if everyFile !=".DS_Store":
            listOfExistingBugs.append(everyFile)
            print(everyFile)

    userChoice = input("Which file would you like to ammend? ")
    userChoice = path + userChoice

    print("The file looks like this at the minute: \n")
    with open (userChoice, "r") as f:
        for orgionalText in f.readlines():
            print(orgionalText)
            
    textToAdd = input("What would you like to add to the file? ")
    textToAdd = "\n\n" + TodaysDate() + "   " + textToAdd

    with open (userChoice, "a") as f:
        f.write(textToAdd)

    return

def TodaysDate():
    today = datetime.now()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    hour = datetime.now().hour
    minute = datetime.now().minute
    
    monthDict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
            7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

    month = monthDict[int(month)]

    timeRightNow = str(hour) + ":" + str(minute)
    
    TodaysDateString = day + ":" + month + ":" + year
    Result = timeRightNow + "   " + TodaysDateString + ":"

    return(str(Result))


# #close the request
def closeRequest():
    cwd = os.getcwd()
    oldpath = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Requests/"

    listOfCompletedFile = [] 
    counter = 1
    print("All files:")

    for everyFile in os.listdir(oldpath):
        if everyFile != ".DS_Store":
            print(str(counter) + ") " + everyFile)
            counter = counter + 1
            listOfCompletedFile.append(everyFile)
        
    pickedOption = input("Which bug has been finished with? Number: ")
    pickedOption = int(pickedOption) - 1
    pickedOption = listOfCompletedFile[pickedOption]
    addCompletedToFile = oldpath + pickedOption

    textToAdd = "\n\n" + TodaysDate() + "   " + "Completed"

    with open(addCompletedToFile, 'a') as f:
        f.write(textToAdd)

    source = oldpath + pickedOption
    destination = #fullpathtofolder + projectName + "/Completed/" 
    os.chdir(destination) 
    with open (pickedOption, "w") as f:
        f.write("")
    
    locationOfCompleted = destination + pickedOption
    destination = os.path.join(os.path.dirname(source), locationOfCompleted)
    
    os.rename(source, destination)

    print("Files moved")
    
def viewRequest():
    cwd = os.getcwd()
    path = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Requests"
    for everyFile in os.listdir(path):
        if everyFile != ".DS_Store":    
            print(everyFile)
    
    fileToView = input("Which file would you like to view? ")
    fileToView = path + "/" + fileToView

    with open (fileToView, "r") as f:
        for everyLine in f.readlines():
            print(everyLine)

    pass    

def viewListofBugs():
    cwd = os.getcwd()
    oldpath = cwd + "/Projects/Learning/Bug_Tracker/" + projectName + "/Requests"

    listOfCompletedFile = [] 
    counter = 1
    print("All files:")

    for everyFile in os.listdir(oldpath):
        if everyFile != ".DS_Store":
            print(str(counter) + ") " + everyFile)
            counter = counter + 1
            listOfCompletedFile.append(everyFile)

# while True:
    #create the menu 
# def AddEditAmendCloseBugs(New_Request, AmmendRequest, closeRequest, viewRequest, viewListofBugs):
def AddEditAmendCloseBugs():    
    userOption = input("What would you like to do? \n(1) Create a new request (2) Ammend an existing request (3) Close a request (4) View a bug ticket? \n")

    if userOption == "1":
        New_Request() #this is for adding a new bug
    elif userOption == "2":
        AmmendRequest() #this adds to a new bug, and time and date stampped
    elif userOption == "3":
        closeRequest() #this closes the request and moves it to the comlpeted folder
    elif userOption == "4":
        viewListofBugs() #views a list of the bugs
        newOption = input("Would you like to edit a file? Y/N ")
        if newOption == "Y":
            viewRequest()  #this prints out the entire file
    elif userOption != "1" or userOption != "2" or userOption != "3" or userOption != "4":
        pass
    # break

def projectNameCheck():
    # while True:
    print("What is the Project Name?")
    projectName = str(input())
    path = #full path to folder
    projectPath = path + projectName
    #if folder exists
    try:
        if not os.path.exists(projectPath):
            print("This does not exist would you like to make a new folder?")
            answer = input()
            if answer == "y": 
                os.mkdir(projectPath)
                print("folder created")
                os.mkdir (projectPath + "/Requests")
                os.mkdir (projectPath + "/Completed")
                print("Subfolders created")
            else:
                print("A new folder wasn't  made. Please run again with the correct name or a new name that you want to use.")
    except OSError:
        print ("There was an error finding the folder path")
    else:
        pass
    return projectName,projectPath

projectName, projectPath= projectNameCheck()

if os.path.exists(projectPath):
    AddEditAmendCloseBugs()
# os.chdir (projectPath)
# print(projectPath)
