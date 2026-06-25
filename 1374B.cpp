// #include<iostream>
// using namespace std;
// int main(){
//       int t;
//       cin>>t;
//       while(t--){
//           int n;
//           cin>>n;
//           int operations=0;
//           int a=6;
//           while(1)
//           {
//             if(n%a!=0){
//                  n=n*2;
//                  if(n%a!=0){
//                       n=n*2;
//                       if(n%a!=0){
//                         if(operations>0){
//                         cout<<operations;
//                         break;
//                         }
//                         else{cout<<"-1";
//                              break;
//                             }
//                       }
//                       else{operations++;}
//                       n=n/6;
//                  }
//                  else{operations++;}
//                  n=n/6;
//             }
//             else{operations++;}
//             n=n/6;
//           }   
//       }
// }
#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long n;
        cin >> n;

        int count2 = 0, count3 = 0;

        // Count how many times divisible by 2
        while (n % 2 == 0) {
            n /= 2;
            count2++;
        }

        // Count how many times divisible by 3
        while (n % 3 == 0) {
            n /= 3;
            count3++;
        }

        // If n still > 1 → it had other prime factors (impossible)
        if (n != 1) {
            cout << -1 << endl;
            continue;
        }

        // You can only make it 1 if there are enough 3s to match 2s
        if (count3 < count2) {
            cout << -1 << endl;
        } else {
            // Each "divide by 6" uses one 2 and one 3
            // For extra 3s, you must multiply by 2 before dividing
            cout << (count3 - count2) + count3 << endl;
        }
    }
    return 0;
}
