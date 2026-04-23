#include <iostream>
using namespace std;

// int main(){
//     int a,b;
//     cout<<"Enter a numbers a and b";
//     cin>>a>>b;
//     if (a>b){
//         cout<<a;
//     }
//     else
//         cout<<b;
// }

// int main(){
//     int sum=0;
//     for (int i = 0; i < 10; i++)
//     {
//         sum=sum+i;
//     }
//     cout<<sum;
// }

// int decTOBinary(int decNum)
// {
//     int ans = 0, pow = 1;
//     while (decNum > 0)
//     {
//         int rem = decNum % 2;
//         decNum /= 2;
//         ans += (rem * pow);
//         pow *= 10;
//     }

//     return ans;
// }
// int main()
// {
//     int decNum = 20;
//     cout << decTOBinary(20) << endl;
//     //for 1 to 10
//     // for (int i = 1; i <= 10; i++)
//     // {
//     //     cout << decTOBinary(i) << endl;
//     // }

//     return 0;
// }

// int binarytodec(int binNum)
// {
//     int ans = 0, pow = 1;
//     while (binNum > 0)
//     {
//         int rem = binNum % 10;
//         ans += (rem * pow);
//         binNum /= 10;
//         pow *= 2;
//     }

//     return ans;
// }
// int main()
// {
//     cout << binarytodec(10100) << endl;

//     return 0;
// }

int power(int num){
    int div;
    while(num>=0){
        div=num%2;
        cout<<div;
    }
    // if (num==0){
    //     cout<<"true";
    // }
    // else{
    //     cout<<"false";
    // }
}

int main(){
    int n;
    cout<<"Entera number";
    cin>>n;
    cout<<power(32);

}