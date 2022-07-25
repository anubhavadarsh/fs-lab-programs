import sys
from typing import List


def checkMaxLen(val: str, max: int):
    if len(val) > max:
        print(f"exceeds maximum specified length {max}")
        sys.exit()

    return val


class Student:
    # private data members
    __USNMAX = 15
    __NAMMAX = 15
    __BRNMAX = 10

    def __init__(self, filename):
        self.filename = filename
        self.__rrnList: List[int] = []
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
            self.__rrnList.append(f.tell())
            f.write(f"{record}\n")

    def unpack(self, record):
        [usn, name, branch, *_] = record.split("|")
        print(f"usn: {usn} name: {name} branch: {branch}")

    def display(self):
        if len(self.__rrnList) == 0:
            print(f"No records to be displayed!")
            return

        with open(self.filename, "r") as f:
            records = [record.strip() for record in f.readlines()]

            for re in records:
                self.unpack(re)

    def searchByRRN(self):
        if len(self.__rrnList) == 0:
            print(f"No records to search!")
            return

        rrn = int(input("enter rrn to search: "))

        if rrn > len(self.__rrnList) - 1:
            print(f"Record with RRN {rrn} not found!")
            return

        with open(self.filename, "r") as f:
            f.seek(self.__rrnList[rrn])
            self.unpack(f.readline().strip())


if __name__ == "__main__":
    filename = input("enter a filename to continue: ")

    stu = Student(filename)

    while True:
        ch = int(
            input(
                "\n1. Insert\n2. Display\n3. Search by RRN\n4. Exit\
				\nPlease choose an option to continue: "
            )
        )

        if ch == 1:
            stu.insRecord()
        elif ch == 2:
            stu.display()
        elif ch == 3:
            stu.searchByRRN()
        elif ch == 4:
            break
        else:
            print("enter correct choice!")
