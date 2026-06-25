#include <iostream>
#include <vector>
using namespace std;
int main(){
    int no_of_problems;
    int solutions=0;
    int count=0;
    cin>>no_of_problems;
    vector<vector<int>> answers(no_of_problems, vector<int>(3,0)); //NEW 

    //input
    for (int i = 0; i < no_of_problems; i++)
    {
       cin>>answers[i][0];
       cin>>answers[i][1];
       cin>>answers[i][2];
    }
    
    for (int i = 0; i < no_of_problems; i++)
    {   if(answers[i][0]==1) count++;            //mistaek: double '=' to check value
        if(answers[i][1]==1) count++;
        if(answers[i][2]==1) count++;
        
        if(count >=2){
            solutions++;
        }
        count=0;
    }
     
    cout<<solutions;
}