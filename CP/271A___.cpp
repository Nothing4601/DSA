//Write long and wrong code but logig is wright

//1st Method
// #include <iostream>
// using namespace std;
// int main(){
//        int year;
//        cin>>year;
//        while(1){
//           year++; //ex: abcd
//           int a = year/1000;
//           int b= (year/100)%10;
//           int c= (year/10)%10;
//           int d= year%10;
//           if(a!=b && a!=c && a!=d && b!=c && b!=d && c!=d){
//             cout<<year;
//             break;
//           }
//         } 
// }

//2nd Method

 #include <iostream>
 #include<set>
 using namespace std;

 int main(){
       int year;
       cin>>year;
       while(1){
        year++;
        string s=to_string(year);
        set<char> digits(s.begin(),s.end()); // store only distinct number in set
        if(digits.size()==s.size()) {cout<<year; break;}

       }
 }

