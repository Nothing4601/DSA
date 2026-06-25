#include<iostream>
using namespace std;
int main(){
      int numbers[4];
      int answers[3];
      int j=0;
      int max=0;
      int max_index=0;
      //input and find maximum number and it's index
      for(int i=0; i<4; i++){
         cin>>numbers[i];
        // max=numbers[0]; yhis is mistake always define max=numbers[0]
          if(numbers[i]> max){
               max=numbers[i];
               max_index=i;
          }
      }
      
      for(int i=0; i<4; i++){
        if(i != max_index){
            answers[j]=numbers[max_index] - numbers[i];
            j++;
        }
      }
     
      cout<<answers[0]<<" "<<answers[1]<<" "<<answers[2]<<endl;


}