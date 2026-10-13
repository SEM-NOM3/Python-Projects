import os

def openfile(): 
    if os.path.exists("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt"):
        with open ("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt", "r") as f:
            print(f.read())
    else:
        print("The file does not exist")

openfile()

while True:
    Choice = input("Do you want to see your notes, add or delete a note? (a/d/s/n): ")
    if Choice.lower() == "a":
        f = open("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt", "a")
        NewNote = input("Write your note here: ")
        f.write("\n" + NewNote + ";")
        f.close()
    elif Choice.lower() == "d":
        deleteLn = input("Enter the line number you want to delete: ")
        if os.path.exists("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt"):
            with open("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt", "r") as f:
                lines = f.readlines()
                if int(deleteLn)  == 1:
                    print("You cant delete the first line, it is reserved for the title of the notes")
                elif int(deleteLn) <= len(lines):
                    del lines[int(deleteLn)-1]
                    with open("C:\\Users\\dinic\\OneDrive\\Documentos\\VS projects\\Project Nelly\\Study\\Projects\\Owns\\Personal Notes\\PNotes.txt", "w") as f:
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
