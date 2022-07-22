def match(f1Name, f2Name):
    names1File = open(f1Name, "r")
    names2File = open(f2Name, "r")

    matchFile = open("merge.txt", "w")

    print("matched names are: ")

    name1 = names1File.readline().strip()
    name2 = names2File.readline().strip()

    while name1 and name2:
        if name1 == name2:
            matchFile.write(f"{name1}\n")
            print(name1, end="\n")
            name1 = names1File.readline().strip()
            name2 = names2File.readline().strip()
        elif name1 < name2:
            name1 = names1File.readline().strip()
        else:
            name2 = names2File.readline().strip()

    names1File.close()
    names2File.close()
    matchFile.close()


if __name__ == "__main__":

    f1Name = "names1.txt"
    f2Name = "names2.txt"
    print(f"matching files {f1Name} and {f2Name}")

    match(f1Name, f2Name)
