#include<iostream>
#include<vector>
using namespace std;
// int main(){
//      int cases;
//      cin>>cases;
//      vector<int> input(cases);
//      vector<int> floor(cases);
//      vector<int> output(cases);
//      for (int i = 0; i < cases; i++)
//      {
//            cin>>input[i];
//      }
     
//      for (int j = 0; j < cases; j++)
//      {
//         floor[j]=input[j] % 10;
//      }
//      for()


// }
int main(){
    int t;
    cin>>t;
    while(t--){
          
          int floor;
          int no_of_digit;
          int input;
          cin>>input;
          floor=input % 10;
          if(input /1000 != 0) no_of_digit=4;
          else if(input/100 !=0) no_of_digit=3;
          else if(input/10 != 0) no_of_digit=2;
          else{ no_of_digit=1;}
          cout<< (floor-1)*10 + no_of_digit*(no_of_digit+1)/2<<endl;

    }
}