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

    names = []
    for file in files:
        fileContent = [content.strip() for content in file.readlines()]
        names.extend(fileContent)

    names.sort()

    with open("merge.txt", "w") as f:
        f.writelines([name + "\n" for name in names])
