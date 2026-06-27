try:
    with open("notes.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.Creating a new file...")