#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
       int n;
       cin>>n;
       int k=0;
       int a[n];
       for (int i = 0; i < n; i++)
       {
         cin>>a[i];
         if(a[i]==2){k+=1;}
       }
      
       if (k==0 ){cout<< "1"<<endl;}
       else if (k%2 != 0 ){cout<< "-1"<<endl;}
       else{  int b=0;
        for (int j = 0; j < n; j++){
            if (a[j]==2){
                b=b+1;
            }
            if(b==k/2){
                cout<< j+1<<endl;
                break;
            }
        }
    }
    }
}