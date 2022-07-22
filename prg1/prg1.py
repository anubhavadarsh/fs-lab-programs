def stdToStd():
    n = int(input("enter the number of records: "))
    arr = []

    print("enter names: ")
    for i in range(n):
        name = input()
        arr.append(name.strip())

    print("reversed names: ")
    for name in arr:
        print(name[::-1], end="\n")


def fileToFile():
    iFname = input("Enter the input file name: ")
    ifile = open(iFname, "r")
    names = [
        name.strip() for name in ifile.readlines()
    ]  # remove newline from the end of the records

    with open("outputFile.txt", "w") as f:
        for name in names:
            f.write(f"{name[::-1]}\n")


if __name__ == "__main__":
    while True:
        print("\n1. std input to std output\n2. file to file\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            stdToStd()
        elif ch == 2:
            fileToFile()
        else:
            break
