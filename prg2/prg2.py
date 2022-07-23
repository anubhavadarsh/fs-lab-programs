import sys


def checkMaxLen(val: str, max: int):
    if len(val) > max:
        print("exceeded maximum limit!")
        sys.exit()

    return val


INSERT = "INSERT"
EDIT = "EDIT"


class Student:
    # private data members:
    __USNMAX = 10
    __NAMMAX = 10
    __BRNMAX = 5

    __moveto = 0

    def __init__(self, filename):
        self.filename = filename
        self.recordsNum = 0
        self.initializeFile()

    def initializeFile(self):
        f = open(self.filename, "w")
        f.close()

    def pack(self, action):
        usn = checkMaxLen(input("enter usn: "), self.__USNMAX)
        name = checkMaxLen(input("enter name: "), self.__NAMMAX)
        branch = checkMaxLen(input("enter branch: "), self.__BRNMAX)

        buffer = usn + "|" + name + "|" + branch + "|"
        if len(buffer) < 28:
            buffer = buffer + "#" * (28 - len(buffer))

        mode = "a" if action == INSERT else "r+"
        with open(self.filename, mode) as f:
            if action == EDIT:
                f.seek(self.__moveto)
            f.write(f"{buffer}\n")
            if action == INSERT:
                self.recordsNum = self.recordsNum + 1

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

    def search(self):
        key = checkMaxLen(input("enter usn to search: "), self.__USNMAX)

        with open(self.filename, "r+") as f:
            for i in range(self.recordsNum):
                record = f.readline()
                [usn, *_] = record.split("|")

                if usn == key:
                    print("Record Found!")
                    self.unpack(record)

                    ch = int(input("Do you wish to modify? enter 1 to do so: "))
                    if ch == 1:
                        self.__moveto = (
                            f.tell() - 30
                        )  # substract 30(including newline) character from curr pos to move to the line beginning
                        self.pack(EDIT)

                    return

            print("Record not found!")


if __name__ == "__main__":

    filename = input("Enter the file name: ")
    stu = Student(filename)

    while True:
        ch = int(
            input(
                "1. Insert\n2. Display\n3. Search and Modify\n4. Exit\nEnter your choice: "
            )
        )
        if ch == 1:
            stu.pack(INSERT)
        elif ch == 2:
            stu.display()
        elif ch == 3:
            stu.search()
        elif ch == 4:
            break
        else:
            print("Invalid choice!")
