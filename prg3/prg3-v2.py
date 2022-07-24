import sys
import os


def checkMaxLen(val: str, max: int):
    if len(val) > max:
        print(f"exceed maximum specified length {max}")
        sys.exit()

    return val


class Student:
    # private data members:
    __USNMAX = 15
    __NAMMAX = 15
    __BRNMAX = 10

    __outfile = "out.txt"

    def __init__(self, filename):
        self.filename = filename
        self.recordsNum = 0
        self.__initializeFile()

    def __initializeFile(self):
        f = open(self.filename, "w")
        f.close()

    def pack(self):
        print("enter details for student")
        usn = checkMaxLen(input("usn: "), self.__USNMAX)
        name = checkMaxLen(input("name: "), self.__NAMMAX)
        branch = checkMaxLen(input("branch: "), self.__BRNMAX)

        buffer = usn + "|" + name + "|" + branch + "|"
        return buffer

    def insRecord(self):
        record = self.pack()

        with open(self.filename, "a") as f:
            f.write(f"{record}\n")

        self.recordsNum = self.recordsNum + 1

    def unpack(self, record):
        [usn, name, branch, *_] = record.split("|")
        print(f"usn: {usn} name: {name} branch: {branch}")

    def display(self):
        if self.recordsNum == 0:
            print(f"No records to be displayed!")
            return

        with open(self.filename, "r") as f:
            records = [record.strip() for record in f.readlines()]

            for re in records:
                self.unpack(re)

    def searchAndModify(self):
        if self.recordsNum == 0:
            print(f"No records to search!")
            return

        key = checkMaxLen(input("enter the usn to search: "), self.__USNMAX).strip()

        outFile = open(self.__outfile, "w")
        reFile = open(self.filename, "r+")
        for i in range(self.recordsNum):
            record = reFile.readline().strip()
            [usn, *_] = record.split("|")

            if usn == key:
                print("record found!")
                self.unpack(record)

                ch = int(input("Do you wish to modify? press 1 to do so: "))

                if ch == 1:
                    newRecord = self.pack()
                    outFile.writelines([f"{newRecord}\n"] + reFile.readlines())
                    reFile.close()
                    outFile.close()
                    os.remove(self.filename)
                    os.rename(self.__outfile, self.filename)

                    print("new record written successfully!")

                    break

                outFile.close()
                os.remove(self.__outfile)

            outFile.write(f"{record}\n")


if __name__ == "__main__":
    filename = input("enter a filename to continue: ")

    stu = Student(filename)

    while True:
        ch = int(
            input(
                "\n1. Insert\n2. Display\n3. Search and Modify\n4. Exit\
                \nPlease choose an option to continue: "
            )
        )

        if ch == 1:
            stu.insRecord()
        elif ch == 2:
            stu.display()
        elif ch == 3:
            stu.searchAndModify()
        else:
            break
