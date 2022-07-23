import sys


if __name__ == "__main__":
    files = [
        open("n1.txt", "r"),
        open("n2.txt", "r"),
        open("n3.txt", "r"),
        open("n4.txt", "r"),
        open("n5.txt", "r"),
        open("n6.txt", "r"),
        open("n7.txt", "r"),
        open("n8.txt", "r"),
    ]

    mergeFile = open("merge.txt", "w")

    names = []
    for file in files:
        fileContent = file.readline().strip()
        names.append(fileContent)

    while True:
        low = 0
        for i in range(8):
            if names[i] < names[low]:
                low = i

        if names[low] == "~":
            mergeFile.close()
            for file in files:
                file.close()
            sys.exit()

        mergeFile.write(f"{names[low]}\n")
        print(names[low])
        names[low] = files[low].readline().strip()

        if names[low] == "":
            names[low] = "~"
