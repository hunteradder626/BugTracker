import os
import shutil
from datetime import datetime, time

#create a new request
def New_Request():
    bugSubject = input("What is the nature of the bug you have found? ")
    bugBody = input("What can you tell me about the bug? ")
    bugReport = "Title:     " + bugSubject + "\n\n" + "Body:    " + bugBody
    
    #go into the request folder
    #highest number from the files stored?
    cwd = os.getcwd()
    # print(cwd)

    path = cwd + "/Projects/Learning/Bug_Tracker/Requests"
    # print(path)

    os.chdir(path)
    listOfFileNames = []

    for eachFile in os.listdir(path):
        if eachFile != ".DS_Store":
            fileName = []
            fileName = eachFile.split()
            listOfFileNames.append(int(fileName[0]))
            # print(listOfFileNames)

    if listOfFileNames == []:
        bugNumber = 1
    else:    
        listOfFileNames.sort()
        bugNumber = listOfFileNames[-1] + 1

    # #store the request
    request = str(bugNumber) + " " + bugSubject + ".txt"

    with open (request, 'w') as f:
        f.write(bugReport)    
    
    return bugSubject,bugReport,bugNumber

# bugSubject, bugReport, bugNumber = New_Request()

#ammend request
def AmmendRequest():
    cwd = os.getcwd()
    path = cwd + "/Projects/Learning/Bug_Tracker/Requests"
    listOfExistingBugs = []
    
    print("All files:")
    for everyFile in os.listdir(path):
        if everyFile !=".DS_Store":
            listOfExistingBugs.append(everyFile)
            print(everyFile)

    userChoice = input("Which file would you like to ammend? ")
    userChoice = path + "/" + userChoice

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
    oldpath = cwd + "/Projects/Learning/Bug_Tracker/Requests/"

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

    textToAdd = "\n\n" + TodaysDate() + "   " + "Completed"

    with open(pickedOption, 'a') as f:
        f.write(textToAdd)

    source = oldpath + pickedOption
    destination = "/Projects/Learning/Bug_Tracker/Completed/" 
    os.chdir(destination) 
    with open (pickedOption, "w") as f:
        f.write("")
    
    locationOfCompleted = destination + pickedOption
    destination = os.path.join(os.path.dirname(source), locationOfCompleted)
    
    os.rename(source, destination)

    print("Files moved")
    
def viewRequest():
    cwd = os.getcwd()
    path = cwd + "/Projects/Learning/Bug_Tracker/Requests/"
    for everyFile in os.listdir(path):
        if everyFile != ".DS_Store":    
            print(everyFile)
    
    fileToView = input("Which file would you like to view? ")
    fileToView = path + "/" + fileToView

    with open (fileToView, "r") as f:
        for everyLine in f.readlines():
            print(everyLine)

    pass    

#create the menu
userOption = input("What would you like to do? (1) Create a new request (2) Ammend an existing request (3) Close a request (4) View a bug ticket? ")

if userOption == "1":
    New_Request() #this is for adding a new bug
elif userOption == "2":
    AmmendRequest() #this adds to a new bug, and time and date stampped
elif userOption == "3":
    closeRequest() #this closes the request and moves it to the comlpeted folder
elif userOption == "4":
    viewRequest()  #this prints out the entire file
#view list of bugs option, followed by view request?      
else:
    "Please enter an option 1 to 3"
