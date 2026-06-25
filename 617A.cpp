#include <iostream>
using namespace std;
int main(){
     int distance;
     cin>>distance;
     int step=0;

     if(distance % 5 == 0) step=distance/5;
     else{ int x=distance/5;
        step= x + 1;
    }
    cout<<step;
}

