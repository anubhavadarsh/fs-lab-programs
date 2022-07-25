from dataclasses import dataclass
from typing import List
import sys


def checkMaxLen(val: str, max: int):
    if len(val) > max:
        print(f"exceeds maximum specified length {max}")
        sys.exit()

    return val


@dataclass
class PrimaryIndex:
    key: str = ""
    offset: int = 0


class Student:
    # private data members
    __USNMAX = 15
    __NAMMAX = 15
    __BRNMAX = 10

    def __init__(self, filename):
        self.filename = filename
        self.__indexList: List[PrimaryIndex] = []
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

    def unpack(self, record):
        [usn, name, branch, *_] = record.split("|")
        print(f"usn: {usn} name: {name} branch: {branch}")

    def insRecord(self):
        record = self.pack()

        [usn, *_] = record.split("|")
        pos = self.search(usn)

        if pos != -1:
            print(f"record with key: {usn} already exists!")
            return

        with open(self.filename, "a") as f:
            self.__indexList.append(PrimaryIndex(usn, f.tell()))
            f.write(f"{record}\n")

        self.__indexList.sort(key=(lambda index: index.key))

    def delRecord(self):
        usn = checkMaxLen(input("enter usn to delete record: "), self.__USNMAX)

        pos = self.search(usn)

        if pos == -1:
            print(f"record with key: {usn} doesn't exists")
            return

        with open(self.filename, "r+") as f:
            f.seek(self.__indexList[pos].offset)
            f.write("*")
            print(f"record with key: {usn} deleted  successfully!")

        self.__indexList = list(
            filter(lambda index: index.key != usn, self.__indexList)
        )

    def search(self, usn):
        low = 0
        high = len(self.__indexList) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if usn == self.__indexList[mid].key:
                return mid
            elif usn < self.__indexList[mid].key:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return -1

    def display(self):
        if len(self.__indexList) == 0:
            print("no records to be displayed!")
            return

        print("\t" + "-" * 16 + "\t")
        print("\t" + "Primary Index" + "\t")
        print("\t" + "-" * 16 + "\t")
        print("\tkey\toffset\t")
        print("\t" + "-" * 16 + "\t")

        for index in self.__indexList:
            print(f"\t{index.key}\t{index.offset}\t")

        with open(self.filename, "r") as f:
            for index in self.__indexList:
                f.seek(index.offset)

                self.unpack(f.readline().strip())

    def searchRecord(self):
        usn = input("enter usn to search record: ")

        pos = self.search(usn)

        if pos == -1:
            print(f"record with key: {usn} doesn't exists!")
            return

        with open(self.filename, "r") as f:
            f.seek(self.__indexList[pos].offset)
            self.unpack(f.readline().strip())


if __name__ == "__main__":
    filename = input("enter filename to continue: ")

    stu = Student(filename)

    while True:
        ch = int(
            input(
                "\n1. Insert\n2. Delete\n3. Display\n4. Search\n5. Exit\
                \nEnter your choice: "
            )
        )

        if ch == 1:
            stu.insRecord()
        elif ch == 2:
            stu.delRecord()
        elif ch == 3:
            stu.display()
        elif ch == 4:
            stu.searchRecord()
        elif ch == 5:
            break
        else:
            print("Invalid choice!\n")
