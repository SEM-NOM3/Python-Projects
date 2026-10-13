#Dont forget to change the file path

import os

FilePath = "C:\\Users\\User\\Downloads\\Personal Notes\\PNotes.txt"
deleteLn = None
Choice = None
NewNote = None
lines = None

def openfile(): 
    if os.path.exists(FilePath):
        with open (FilePath, "r") as f:
            print(f.read())
    else:
        print("The file does not exist")

openfile()

while True:
    Choice = input("Do you want to see your notes, add or delete a note? (a/d/s/n): ")
    
    if Choice.lower() == "a":
        f = open(FilePath, "a")
        NewNote = input("Write your note here: ")
        f.write("\n" + NewNote + ";")
        f.close()
    elif Choice.lower() == "d":
        deleteLn = input("Enter the line number you want to delete: ")
        if os.path.exists(FilePath):
            with open(FilePath, "r") as f:
                lines = f.readlines()
                if int(deleteLn)  == 1:
                    print("You cant delete the first line, it is reserved for the title of the notes")
                elif int(deleteLn) <= len(lines):
                    del lines[int(deleteLn)-1]
                    with open(FilePath, "w") as f:
                        f.writelines(lines)
                else:
                    print("The line number is out of range")
        else:
            print("The file does not exist")

    elif Choice.lower() == "s":
        openfile()
    elif Choice.lower() == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'a', 'd', 's', or 'n'.")
