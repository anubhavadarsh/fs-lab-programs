#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<process.h>
void main()
{
 fstream fp1,fp2;
 char fin[10],fout[10];
 int ch,n,i;
 char str[10],name[10][10];
 clrscr();
 for(;;)
 {
 cout<<"1:Std Input to Std Output 2:File to Std Output 3:File to File\n";
 cout<<"Enter your Choice : ";
 cin>>ch;
 switch(ch)
 {
 case 1: cout<<"Enter Number of Records : ";
 cin>>n;
 cout<<"Enter "<<n<<" Names : ";
 for(i=0;i<n;i++)
 {
 cin>>name[i];
 }
 cout<<"Reversed names are ... "<<endl;
 for(i=0;i<n;i++)
 {
 strrev(name[i]);
 cout<<name[i];
 cout<<"\n";
 }
 break;
case 2: cout<<"Enter the Input Filename : ";
 cin>>fin;
 fp1.open(fin,ios::in);
 while(!fp1.fail())
 {
 fp1>>str;
 strrev(str);
 cout<<str;
 cout<<"\n";
 }
 fp1.close();
 break;
 case 3: cout<<"Enter the Input Filename : ";
 cin>>fin;
 cout<<"Enter the Output Filename : ";
 cin>>fout;
 fp1.open(fin,ios::in);
 fp2.open(fout,ios::out);
 while(!fp1.fail())
 {
 fp1>>str;
 strrev(str);
 fp2<<str;
 fp2<<"\n";
 }
 fp1.close();
 fp2.close();
 break;
 default: exit(0);
 }
 }
}
