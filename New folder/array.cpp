// To find smallest and alrgest numbers with their index numbers.
// #include<iostream>
// using namespace std;
// int main(){
//     int nums[]={2,3,4,-1};
//     int size=4;
//     int smallest=INT16_MAX;
//     int largest=INT16_MIN;
//     int min_index;
//     int max_index;
//      for(int i=0;i<size;i++){
//         if(nums[i] < smallest){
//             smallest = nums[i];
//             min_index = i;
//         }

//         if(nums[i] > largest){
//             largest = nums[i];
//             max_index = i;
//         }
//     }
//     cout<<smallest<<"  min_index = "<<min_index<<endl;
//     cout<<largest<<"   max_index = "<<max_index;
// }

// Linear search
#include <iostream>
using namespace std;
int linearsearch(int array[],int size,int target){
    for(int i=0;i<size;i++){
        if(array[i]==target){
            return i;
        }
        return -1;
    }

}
int main(){
    int array[]={2,4,6,8,9};
    int size=5;
    int target=6;
    cout<<linearsearch(array,size,target);
    return 0; 
}