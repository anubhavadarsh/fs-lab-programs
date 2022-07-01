/*
Write a C++ program to read and write student objects with Variable - Length records
using any suitable record structure. Implement pack(), unpack(), modify() and search()
methods.
*/

#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <conio.h>
#include <process.h>

using namespace std;

fstream fp1, fp2;
int n = 0;
char fname[10];

class Student {
private:
	char usn[10], name[15], branch[5];
public:
	void pack(int a) {
		char buffer[100];
		cout<<"Enter the student usn, name, branch";
		strcpy(buffer, usn);
		strcat(buffer, "|");
		strcat(buffer, name);
		strcat(buffer, "|");
		strcat(buffer, branch);

		if(a == 1) {
			fp1 << buffer;
			fp1 << "\n";
		} else {
			fp2 << buffer;
			fp2 << "\n";
		}
	}

	void display() {
		char buffer[150];
		cout<<"\n File contents are \n";
		fp1.open(fname, ios::in);
		for(int i = 1; i <= n; ++i) {
			fp1 >> buffer;
			unpack(buffer);
		}

		fp1.close();
	}

	void unpack(char buffer[]) {
		char *t;
		t = strtok(buffer, "|");
		cout<<"\nusn: "<<t<<endl;
		cout<<" name: "<<t<<endl;
		t = strtok(NULL, "\0");
		cout<<" Branch: "<<t<<endl;
	}

	void search() {
		char buffer[100], temp[100];
		char* usn;
		char key[15];
		int i, choice;
		cout<<"\n Enter usn to search: ";
		cin>>key;
		fp1.open(fname, ios::in);
		fp2.open("out.txt", ios::out);
		for(i = 1; i <= n; ++i) {
			fp1 >> buffer;
			strcpy(temp, buffer);
			usn = strtok(buffer, "|");
			if(strcmp(usn, key) == 0) {
				cout << "Record Found\n";
				unpack(buffer);
				cout<<"\nDo you wish to modify "<<endl;
				cout<<"\n1. Yes \n2. No";
				cin>>choice;
				if(choice == 1) {
					pack(2);
					while(!fp1.fail()) {
						fp1 >> buffer;
						fp2 << buffer << "\n";
					}

					fp1.close();
					fp2.close();
					remove(fname);
					rename("out.txt", fname);
					return;
				} else {
					fp1.close();
					fp2.close();
					remove("out.txt");
				}
			} else {
				fp2 << buffer;
				fp2 << "\n";
			}
		}

		cout << "Record not found";
		fp1.close();
		fp2.close();
		remove("out.txt");
	}
};

int main() {
	int ch;
	Student s1;
	
	cout<<"Enter filename: ";
	cin>>fname;
	fp1.open(fname, ios::out | ios::app);
	fp1.close();

	for(;;) {
		cout<<"\n1. insert \n2. display \n2. search and modify \n4. exit\n";
		cout<<"Enter your choice: ";
		cin>>ch;
		switch(ch) {
			case 1: {
				n++;
				fp1.open(fname, ios::app);
				s1.pack(1);
				fp1.close();
				break;
			}
			case 2: s1.display(); break;
			case 3: s1.search(); break;
			case 4: exit(0);

			default: cout<<"Invalid Choice\n";
		}
	}
}