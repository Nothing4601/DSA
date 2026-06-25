#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int max_diff=0;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
                cin>>a[i];
        sort(a.begin(), a.end()); //asecnding or increasing

        for (int i = 0; i < n; i+=2){
             int diff=a[i+1] - a[i];
             max_diff=max(diff,max_diff);
         }
        cout<<max_diff<<endl;     
   }  
}