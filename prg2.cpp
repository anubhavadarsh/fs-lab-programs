/* Write a c++ program to read and write student objects with fixed length records and
	the fields delimited by "|". Implement pack(), unpack(), modify() and search() methods
*/

#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>
#include <process.h>

using namespace std;

fstream fp;
int n = 0;
char fname[10];

class student {
private:
	char usn[10], name[10], branch[5];
public:
	void pack() {
		char buffer[28];
		cout<<"Enter the usn, name and branch: ";
		cin>>usn>>name>>branch;
		strcpy(buffer, usn);
		strcat(buffer, "|");
		strcpy(buffer, name);
		strcat(buffer, "|");
		strcpy(buffer, branch);
		strcat(buffer, "|");
		int len = strlen(buffer);
		while(len < 27) {
			strcat(buffer, "#");
			len++;
		}

		buffer[27] = '\0';
		fp<<buffer<<"\n";
	}

	void unpack(char buffer[]) {
		char *t;
		t = strtok(buffer, "|");
		cout<<"usn: "<<t<<endl;
		t = strtok(NULL, "|");
		cout<<"Name: "<<t<<endl;
		t = strtok(NULL, "|");
		cout<<"Branch: "<<t<<endl;
	}

	void display() {
		char buffer [28];
		int i, j;
		if(n == 0) {
			cout<< "No records to display: ";
			return;
		}

		cout<<"\n File contents are: \n";
		fp.open(fname, ios::in);
		for(int i = 1; i <= n; i++) {
			fp>> buffer;
			unpack(buffer);
			cout<<endl;
		}

		fp.close();
	}

	void search() {
		char buffer[28], temp[28];
		char key[15];
		char *usn;
		int i, j, k, choice;
		cout<<"Enter the USN to search: ";
		cin>>key;
		fp.open(fname, ios::in|ios::out);
		for(int i = 1; i <= n; ++i) {
			fp>>buffer;
			strcpy(temp, buffer);
			usn = strtok(buffer, "|");
			if(strcmp(key, usn) == 0) {
				cout<<"\n Records found: ";
				unpack(buffer);
				cout<<endl;
				cout<<"\n Do you wish to modify? \n";
				cout<<"\n Enter your choice \n1. yes\n2. No\n";
				cin>>choice;
				if(choice == 1) {
					fp.seekp(-27,ios::cur);
					pack();
				}

				fp.close();
				return;
			}
		}
		cout<<"Record not found.";
		fp.close();
		getch();
	}
};

int main() {
	int i, ch;
	student s1;

	cout<<"Enter the filename: ";
	cin>>fname;
	fp.open(fname, ios::out|ios::trunc);
	fp.close();
	for(;;) {
		cout<<"\n1. Insert \n2. Display\n3. Search and Modify \n4. Exit\n";
		cout<<"Enter your choice: ";
		cin>>ch;
		switch(ch) {
			case 1: n++;
							fp.open(fname, ios::app);
							s1.pack();
							fp.close();
							break;
			case 2: s1.display();
							break;
			
			case 3: s1.search();
							break;
			case 4: exit(0);
			default:
					cout<<"invalid choice!\n";
		}
	}
}