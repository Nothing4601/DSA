#include <iostream>
#include <vector>
using namespace std;
int main(){
    int cases;
    cin>>cases;
    int negative1=0;
    vector<int> cases_data(cases);     //NEW
    vector<int> operations(cases,0);  //NEW
    
    //input and chek condition
    for (int i = 0; i < cases; i++)
    {
        cin>>cases_data[i];
        vector<int> element(cases_data[i]);
        //check condition
        for (int t = 0; t < cases_data[i]; t++)
        {  
            cin>>element[t];
            if(element[t]==0) operations[i]++;
            if(element[t]==-1) negative1++;
        }
        
        if(negative1 % 2 !=0)operations[i]+=2;
        negative1=0;    
    }
    
    for (int j = 0; j < cases; j++)
    {
        cout<<operations[j]<<endl;
    }
    
}