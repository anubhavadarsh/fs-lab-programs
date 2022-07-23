import sys
import os


def checkMaxLen(val: str, max: int):
    if len(val) > max:
        print("exceeded maximum limit!")
        sys.exit()

    return val


class Student:
    # private data members
    __USNMAX = 15
    __NAMMAX = 15
    __BRNMAX = 5

    def __init__(self, filename):
        self.filename = filename
        self.recordsNum = 0
        self.index = []
        self.__initializeFile()

    def __initializeFile(self):
        file = open(self.filename, "w")
        file.close()

    def pack(self):
        usn = checkMaxLen(input("usn: "), self.__USNMAX)
        name = checkMaxLen(input("name: "), self.__NAMMAX)
        branch = checkMaxLen(input("branch: "), self.__BRNMAX)

        buffer = usn + "|" + name + "|" + branch + "|"

        with open(self.filename, "a") as f:
            self.recordsNum = self.recordsNum + 1
            self.index.append(f.tell())

            f.write(f"{buffer}\n")

    def unpack(self, record):
        [usn, name, branch, *_] = record.split("|")
        print(f"USN: {usn}\nName: {name}\nBranch: {branch}\n")

    def display(self):
        if self.recordsNum == 0:
            print("No records to display!")
            return

        print("\nFile contents are: ")

        with open(self.filename, "r") as f:
            records = [record.strip() for record in f.readlines()]
            for record in records:
                self.unpack(record)

    def searchByRRN(self):
        rrn = int(input("Enter the RRN of the record: "))
        if rrn > self.recordsNum - 1:
            print(f"Record with RRN {rrn} not found!")
            return

        f = open(self.filename, "r")
        f.seek(self.index[rrn])
        self.unpack(f.readline())
        f.close()


if __name__ == "__main__":
    filename = input("Enter file name: ")
    stu = Student(filename)

    while True:
        ch = int(
            input(
                "\n1. Insert\n2. Display\n3. Search by RRN\n4. Exit\nEnter your choice: "
            )
        )

        if ch == 1:
            stu.pack()
        elif ch == 2:
            stu.display()
        elif ch == 3:
            stu.searchByRRN()
        elif ch == 4:
            break
        else:
            print("Invalid choice\n")
