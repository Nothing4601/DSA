#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while (t--)
    {
       int n,k;
       cin>> n >> k ;
       vector<int> array(n);

       for(int i=0; i<n;i++){
        cin>>array[i];
       }
     
      if(k>1 || is_sorted(array.begin(),array.end())) cout<<"YES"<<endl;
      else{cout<<"NO"<<endl;}
    }

}