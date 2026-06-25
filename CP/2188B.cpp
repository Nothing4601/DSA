 #include <iostream>
 #include<set>
 using namespace std;

 int main(){
       int t;
       cin>>t;
       while(t--){
        int n;
        cin>>n;
        char a[n];
        int b=0;
        int c=0;
        int result=0;
        int ones=0;


        for (int i = 0; i < n; i++)
        {
            cin>>a[i];
            a[i]=a[i] - '0';
            if (a[i]==1){
                ones+=1;
                c=i;
                if((c-b-1)%4!=0 & c-b>=4){
                    result+=(int)(c-b-1)/4 +1;
                }
                if((c-b-1)%4==0){result+=(c-b-1)/4; }
                b=i;
            }
        }
        if(ones==0){
            if((n-1)%4!=0 & n>=3){
                    result+=(int)(n-1)/4 +1;
                }
                if((n-1)%4==0){result+=(n-1)/4; }
        }
        cout<<result + ones<<endl;
       }
 }
