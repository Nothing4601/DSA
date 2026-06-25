#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int x;
        int k;
        cin>>x>>k;
        if(x==1 & k==1){cout<<"No"<<endl;continue;}  // 1 is not prime
        if((x==2 || x==3 || x== 5 || x==7) & k==1){cout<<"Yes"<<endl;continue;}
        if(x==1 & k==2){cout<<"Yes"<<endl;continue;} // if K >1 then only case where it is prime
        if(k==1){
            if(sqrt(x)==(int)sqrt(x)){cout<<"No"<<endl;continue;}
            for(int i=2;i<=(int)sqrt(x);i++){
               
                if(x%i==0){cout<<"No"<<endl;break;}
                if(i==(int)sqrt(x)){cout<<"Yes"<<endl;break;}
            }
            
        }
        else{cout<<"No"<<endl;}
    }
}