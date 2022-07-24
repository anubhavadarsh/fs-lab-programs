from dataclasses import dataclass
from typing import List
import sys


def checkMaxLen(val: str, max: int = 10):
    if len(val) > max:
        print("exceeded maximum limit!")
        sys.exit()

    return val


@dataclass  # a mutable alternative to structs
class PrimaryIndex:
    key: str = ""
    offset: int = 0


class Student:
    # private data members
    __USNMAX = 15
    __NAMMAX = 15
    __BRNMAX = 5

    def __init__(self, filename):
        self.filename = filename
        self.recordsNum = 0
        self.__index: List[PrimaryIndex] = []  # set the type for the list
        self.__initializeFile()

    def __initializeFile(self):
        file = open(self.filename, "w")
        file.close()

    def pack(self):
        usn = checkMaxLen(input("usn: "), self.__USNMAX)
        name = checkMaxLen(input("name: "), self.__NAMMAX)
        branch = checkMaxLen(input("branch: "), self.__BRNMAX)

        return usn + "|" + name + "|" + branch + "|"

    def unpack(self, record):
        [usn, name, branch, *_] = record.split("|")
        print(f"USN: {usn}\nName: {name}\nBranch: {branch}\n")

    def insrec(self):
        with open(self.filename, "a") as f:
            record = self.pack()
            [usn, *_] = record.split("|")
            pos = self.search(usn)

            if pos != -1:
                print("record already exists!\n")
                return

            self.recordsNum = self.recordsNum + 1
            self.__index.append(PrimaryIndex(usn, f.tell()))

            f.write(f"{record}\n")
            self.__index.sort(key=(lambda pindex: pindex.key))

    def delrec(self):
        usn = checkMaxLen(input("Enter usn to be deleted: "), self.__USNMAX)
        pos = self.search(usn.strip())

        if pos == -1:
            print("record not found!\n")
            return

        with open(self.filename, "r+") as f:
            f.seek(self.__index[pos].offset)
            f.write("*")

        self.__index = list(
            filter(lambda index: index.key != usn, self.__index)
        )  # filter the records
        self.recordsNum = self.recordsNum - 1

    def search(self, usn):
        low = 0
        high = self.recordsNum - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if self.__index[mid].key == usn:
                return mid
            elif self.__index[mid].key < usn:
                low = mid + 1
            else:
                high = mid - 1
        else:
            return -1

    def display(self):
        if self.recordsNum == 0:
            print("No records to display!")
            return

        print(f"\t{'-'*16}")
        print(f"\tPrimary Index")
        print(f"\t{'-'*16}")
        print(f"\tkey\toffset")
        print(f"\t{'-'*16}")

        for index in self.__index:
            print(f"\t{index.key}\t{index.offset}")

        print("file contents are: ")

        f = open(self.filename, "r")
        for index in self.__index:
            f.seek(index.offset)

            record = f.readline()
            self.unpack(record)

        f.close()

    def searchRecord(self):
        usn = input("Enter the usn to be searched: ")
        pos = self.search(usn.strip())
        if pos == -1:
            print("record not found!\n")
            return

        with open(self.filename, "r") as f:
            f.seek(stu.__index[pos].offset)
            self.unpack(f.readline().strip())

        self.recordsNum = self.recordsNum - 1


if __name__ == "__main__":
    filename = input("Enter file name: ")
    stu = Student(filename)

    while True:
        ch = int(
            input(
                "\n1. Insert\n2. Delete\n3. Display\n4. Search\n5. Exit\nEnter your choice: "
            )
        )

        if ch == 1:
            stu.insrec()
        elif ch == 2:
            stu.delrec()
        elif ch == 3:
            stu.display()
        elif ch == 4:
            stu.searchRecord()
        elif ch == 5:
            break
        else:
            print("Invalid choice!\n")
